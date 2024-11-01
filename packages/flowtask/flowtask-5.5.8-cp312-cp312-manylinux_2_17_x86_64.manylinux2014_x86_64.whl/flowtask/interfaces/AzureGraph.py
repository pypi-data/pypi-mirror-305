import asyncio
from typing import Any, Optional, List, Dict
from datetime import datetime
from azure.identity.aio import (
    ClientSecretCredential,
    OnBehalfOfCredential
)
import msal
from msgraph import GraphServiceClient
from msgraph.generated.models.chat_message_collection_response import (
    ChatMessageCollectionResponse
)
from msgraph.generated.teams.item.channels.get_all_messages.get_all_messages_request_builder import (
    GetAllMessagesRequestBuilder
)
from msgraph.generated.chats.item.messages.messages_request_builder import (
    MessagesRequestBuilder
)
from kiota_abstractions.base_request_configuration import RequestConfiguration
from navconfig.logging import logging
from .client import ClientInterface
from ..conf import (
    MS_TEAMS_TENANT_ID,
    MS_TEAMS_CLIENT_ID,
    MS_TEAMS_CLIENT_SECRET
)
from ..exceptions import ComponentError, ConfigError


logging.getLogger('msal').setLevel(logging.INFO)
logging.getLogger('azure').setLevel(logging.WARNING)

DEFAULT_SCOPES = ["https://graph.microsoft.com/.default"]


def generate_auth_string(user, token):
    return f"user={user}\x01Auth=Bearer {token}\x01\x01"


class AzureGraph(ClientInterface):
    """
    AzureGraph.

    Overview

            Authentication and authorization Using Azure Identity and Microsoft Graph.
    """
    _credentials: dict = {
        "tenant_id": str,
        "client_id": str,
        "client_secret": str,
        "user": str,
        "password": str
    }

    def __init__(
        self,
        tenant_id: str = None,
        client_id: str = None,
        client_secret: str = None,
        scopes: list = None,
        **kwargs,
    ) -> None:
        self.tenant_id = tenant_id or MS_TEAMS_TENANT_ID
        # credentials:
        self.client_id = client_id or MS_TEAMS_CLIENT_ID
        self.client_secret = client_secret or MS_TEAMS_CLIENT_SECRET
        # User delegated credentials:
        self.user = kwargs.pop('user', None)
        self.password = kwargs.pop('password', None)
        self.user_credentials = None
        # scopes:
        self.scopes = scopes if scopes is not None else DEFAULT_SCOPES
        kwargs['no_host'] = True
        kwargs['credentials'] = kwargs.get(
            "credentials", {
                "client_id": self.client_id,
                "tenant_id": self.tenant_id,
                "client_secret": self.client_secret,
                "user": self.user,
                "password": self.password
            }
        )
        super(AzureGraph, self).__init__(
            **kwargs
        )
        self._client = None
        self._graph = None
        self.token_uri = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        self.graph_uri = "https://graph.microsoft.com/v1.0"
        # Logging:
        if not hasattr(self, '_logger'):
            self._logger = logging.getLogger('AzureGraph')

    @property
    def graph(self):
        return self._graph

    @property
    def client(self):
        return self._client

    ## Override the Async-Context:
    async def __aenter__(self) -> "AzureGraph":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        # clean up anything you need to clean up
        return self.close()

    def get_client(self, kind: str = 'client_credentials', token: str = None):
        if not self.credentials:
            raise ConfigError(
                "Azure Graph: Credentials are required to create a client."
            )
        tenant_id = self.credentials.get('tenant_id', self.tenant_id)
        client_id = self.credentials.get('client_id', self.client_id)
        client_secret = self.credentials.get('client_secret', self.client_secret)
        # fix the token URL
        self.token_uri = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        client = None
        # TODO: other type of clients
        if kind == 'client_credentials':
            client = ClientSecretCredential(
                tenant_id=tenant_id,
                client_id=client_id,
                client_secret=client_secret
            )
        elif kind == 'on_behalf_of':
            client = OnBehalfOfCredential(
                client_id=client_id,
                client_secret=client_secret,
                tenant_id=tenant_id,
                user_assertion=token
            )
        return client

    def get_graph_client(self, client: Any, token: str = None, scopes: Optional[list] = None):
        if not scopes:
            scopes = self.scopes
        return GraphServiceClient(credentials=client, scopes=scopes)

    async def get_token(self):
        """
        Retrieves an access token for Microsoft Graph API using ClientSecretCredential.
        """
        if not self._client:
            self._client = self.get_client()
        tenant_id = self.credentials.get('tenant_id', self.tenant_id)
        try:
            # Use the credential to obtain an access token
            token = await self._client.get_token(
                self.scopes[0],
                tenant_id=tenant_id
            )
            self._logger.info(
                "Access token retrieved successfully."
            )
            return token.token, token
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve access token: {e}"
            )
            raise ComponentError(
                f"Could not obtain access token: {e}"
            )

    async def get_user_info(self, user_principal_name: str) -> dict:
        """
        Fetches user information from Microsoft Graph API based on userPrincipalName.

        Args:
            user_principal_name (str): The user principal name (UPN) of the user to fetch info for.

        Returns:
            dict: User information as a dictionary.
        """
        try:
            if not self._graph:
                raise ComponentError(
                    "Graph client not initialized. Please call 'open' first."
                )

            # Fetch the user info using the Graph client
            user_info = await self._graph.users[user_principal_name].get()
            self._logger.info(
                f"Retrieved information for user: {user_principal_name}"
            )
            return user_info
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve user info for {user_principal_name}: {e}"
            )
            raise ComponentError(f"Could not retrieve user info: {e}")

    def user_auth(self, username: str, password: str, scopes: list = None) -> dict:
        tenant_id = self.credentials.get('tenant_id', self.tenant_id)
        authority_url = f'https://login.microsoftonline.com/{tenant_id}'
        client_id = self.credentials.get("client_id", self.client_id)

        if not scopes:
            scopes = ["https://graph.microsoft.com/.default"]
        app = msal.PublicClientApplication(
            authority=authority_url,
            client_id=client_id,
            client_credential=None
        )
        result = app.acquire_token_by_username_password(
            username,
            password,
            scopes=scopes
        )
        if "access_token" not in result:
            error_message = result.get('error_description', 'Unknown error')
            error_code = result.get('error', 'Unknown error code')
            raise RuntimeError(
                f"Failed to obtain access token: {error_code} - {error_message}"
            )
        return result

    def close(self, timeout: int = 1):
        self._client = None
        self._graph = None

    def open(self, **kwargs) -> "AzureGraph":
        """open.
        Starts (open) a connection to Microsoft Graph Service.
        """
        self._client = self.get_client()
        self._graph = self.get_graph_client(self._client)
        self.user = self.credentials.get('user', self.user)
        self.password = self.credentials.get('password', self.password)
        if self.user and self.password:
            self.user_credentials = self.user_auth(
                username=self.user,
                password=self.password,
                scopes=self.scopes
            )
        return self

    async def get_msteams_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        max_messages: Optional[int] = None
    ) -> List[Dict]:
        """
        Fetches messages from a Teams channel.

        Args:
            team_id (str): The ID of the team.
            channel_id (str): The ID of the channel.
            start_time (str, optional): ISO 8601 formatted start time to filter messages.
            end_time (str, optional): ISO 8601 formatted end time to filter messages.
            max_messages (int, optional): Maximum number of messages to retrieve.

        Returns:
            List[Dict]: A list of message objects.
        """
        if not self._graph:
            raise ComponentError(
                "Graph client not initialized. Please call 'open' first."
            )

        messages = []
        print('Credentials <>', self.credentials)
        _filter = f"lastModifiedDateTime gt {start_time!s} and lastModifiedDateTime lt {end_time!s}"
        print('Filter > ', _filter)
        try:
            query_params = GetAllMessagesRequestBuilder.GetAllMessagesRequestBuilderGetQueryParameters(
                filter=_filter
            )

            request_configuration = RequestConfiguration(
                query_parameters=query_params,
            )

            messages = await self._graph.teams.by_team_id(team_id).channels.get_all_messages.get(
                request_configuration=request_configuration
            )

            print('Messages ', messages)
            return messages
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve channel messages: {e}"
            )
            raise ComponentError(
                f"Could not retrieve channel messages: {e}"
            )

    def _is_within_time_range(
        self,
        message_time_str: str,
        start_time: Optional[str],
        end_time: Optional[str]
    ) -> bool:
        """
        Checks if a message's time is within the specified time range.

        Args:
            message_time_str (str): The message's creation time as an ISO 8601 string.
            start_time (str, optional): ISO 8601 formatted start time.
            end_time (str, optional): ISO 8601 formatted end time.

        Returns:
            bool: True if within range, False otherwise.
        """
        message_time = datetime.fromisoformat(message_time_str.rstrip('Z'))

        if start_time:
            start = datetime.fromisoformat(start_time.rstrip('Z'))
            if message_time < start:
                return False

        if end_time:
            end = datetime.fromisoformat(end_time.rstrip('Z'))
            if message_time > end:
                return False

        return True

    async def get_channel_details(self, team_id: str, channel_id: str) -> Dict:
        """
        Fetches details of a Teams channel.

        Args:
            team_id (str): The ID of the team.
            channel_id (str): The ID of the channel.

        Returns:
            Dict: A dictionary containing channel details.
        """
        if not self._graph:
            raise ComponentError(
                "Graph client not initialized. Please call 'open' first."
            )

        try:
            channel_details = await self._graph.teams.by_team_id(team_id).channels.by_channel_id(channel_id).get()

            print('CHANNEL DETAILS > ', channel_details)
            self._logger.info(
                f"Retrieved details for channel: {channel_details.get('displayName')}"
            )
            return channel_details
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve channel details: {e}"
            )
            raise ComponentError(
                f"Could not retrieve channel details: {e}"
            )

    async def get_channel_members(self, team_id: str, channel_id: str) -> List[Dict]:
        """
        Fetches the list of members in a Teams channel.

        Args:
            team_id (str): The ID of the team.
            channel_id (str): The ID of the channel.

        Returns:
            List[Dict]: A list of member objects.
        """
        if not self._graph:
            raise ComponentError(
                "Graph client not initialized. Please call 'open' first."
            )

        members = []
        endpoint = self._graph.teams[team_id].channels[channel_id].members
        query_params = {
            '$top': 50  # Adjust as needed
        }

        # Initial request
        request = endpoint.get(
            query_parameters=query_params
        )

        try:
            # Pagination loop
            while request:
                response = await self._graph.send_request(request)
                response_data = await response.json()

                batch_members = response_data.get('value', [])
                members.extend(batch_members)

                # Check for pagination
                next_link = response_data.get('@odata.nextLink')
                if next_link:
                    # Create a new request for the next page
                    request = self._graph.create_request("GET", next_link)
                else:
                    break

            self._logger.info(
                f"Retrieved {len(members)} members from channel."
            )
            return members
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve channel members: {e}"
            )
            raise ComponentError(f"Could not retrieve channel members: {e}")

    async def find_channel_by_name(self, channel_name: str):
        if not self._graph:

            raise ComponentError(
                "Graph client not initialized. Please call 'open' first."
            )

        # List all teams
        teams = await self._graph.teams.get()
        print(f"Total Teams Found: {len(teams)}")

        for team in teams:
            team_id = team.get('id')
            team_display_name = team.get(
                'displayName',
                'Unknown Team'
            )
            print(f"Checking Team: {team_display_name} (ID: {team_id})")

            # List channels in the team
            channels = await self._graph.list_channels_in_team(team_id)
            print(
                f"Total Channels in Team '{team_display_name}': {len(channels)}"
            )

            # Search for the channel by name
            for channel in channels:
                channel_display_name = channel.get('displayName', '')
                if channel_display_name.lower() == channel_name.lower():
                    channel_id = channel.get('id')
                    print(
                        f"Channel Found: {channel_display_name}"
                    )
                    print(
                        f"Team ID: {team_id}"
                    )
                    print(
                        f"Channel ID: {channel_id}"
                    )

                    # return team_id and channel_id
                    return team_id, channel_id

    async def list_chats(self) -> List[Dict]:
        """
        Lists all chats accessible to the application or user.

        Returns:
            List[Dict]: A list of chat objects.
        """
        if not self._graph:
            raise ComponentError("Graph client not initialized. Please call 'open' first.")

        try:
            chats = []
            chats = await self._graph.users.by_user_id('trocadvrpt@trocglobal.com').chats.get()

            # getting chats from ChatCollectionResponse:
            return chats.value

        except Exception as e:
            self._logger.error(f"Failed to retrieve chats: {e}")
            raise ComponentError(f"Could not retrieve chats: {e}")

    async def find_chat_by_name(self, chat_name: str) -> Optional[str]:
        """
        Finds a chat by its name (topic) and returns its chat_id.

        Args:
            chat_name (str): The name of the chat to find.

        Returns:
            Optional[str]: The chat_id if found, else None.
        """
        chats = await self.list_chats()
        for chat in chats:
            if chat.chat_type.Group == 'group' and chat.topic == chat_name:
                return chat
        return None

    async def get_chat_messages(
        self,
        chat_id: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        max_messages: Optional[int] = None
    ) -> Optional[List]:
        """
        Get chat messages.

        Args:
            chat_id (str): Id of Chat

        Returns:
            Optional[List]: All Chat Messages based on criteria.
        """
        args = {
            "orderby": ["lastModifiedDateTime desc"]
        }
        if max_messages:
            args['top'] = max_messages
        else:
            args['top'] = 50  # max 50 message per-page
        if start_time and end_time:
            args['filter'] = f"lastModifiedDateTime gt {start_time!s} and lastModifiedDateTime lt {end_time!s}"
        query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
            **args
        )
        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        messages = []
        request_builder = self._graph.chats.by_chat_id(chat_id).messages

        try:
            # Initial request
            response = await request_builder.get(
                request_configuration=request_configuration
            )

            # Collect messages from the first response
            if isinstance(response, ChatMessageCollectionResponse):
                messages.extend(response.value)
            else:
                self._logger.warning(
                    f"Unable to find Chat messages over {chat_id}"
                )
            # TODO: add Pagination

            return messages
        except Exception as e:
            self._logger.error(
                f"Failed to retrieve chat messages: {e}"
            )
            raise ComponentError(
                f"Could not retrieve chat messages: {e}"
            )
