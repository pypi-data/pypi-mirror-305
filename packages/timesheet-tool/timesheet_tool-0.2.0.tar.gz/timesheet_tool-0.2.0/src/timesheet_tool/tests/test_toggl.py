# Standard Library
import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

# Local
from timesheet_tool.config import TIMEZONE_OBJ
from timesheet_tool.toggl import TogglClient


class TestTogglClient(TestCase):
    maxDiff = None

    def get_projects_side_effect(self):
        return [
            {
                "id": "0000000",
                "client_id": "0000000",
                "name": "Dummy Project",
                "color": "0",
                "active": True,
            }
        ]

    @patch("requests.get")
    def test__get_projects(self, mock_get):
        client = TogglClient("token")
        mock_get.return_value.json.return_value = {}

        mock_get.assert_called_once_with(
            client.base_url + "/me/projects",
            auth=client.auth,
            timeout=10,
            params={},
        )

    @patch("requests.get")
    def test_get_me(self, mock_get):
        client = TogglClient("token")
        mock_get.return_value.json.return_value = {}

        client.get_me()

        mock_get.assert_called_with(
            client.base_url + "/me", auth=client.auth, timeout=10, params={}
        )

    @patch("requests.get")
    def test_get_project(self, mock_get):
        client = TogglClient("token")
        mock_get.return_value.json.return_value = {}

        project_id = 1
        client.get_project(project_id)

        mock_get.assert_called_with(
            f"{client.base_url}/projects/{project_id}",
            auth=client.auth,
            timeout=10,
            params={},
        )

    @patch("timesheet_tool.toggl.TogglClient.serialize_time_entries")
    @patch("requests.get")
    def test_get_time_entries(self, mock_get, mock_serialize):
        client = TogglClient("token")
        mock_get.return_value.json.return_value = {}

        start_date = "2020-01-01"
        end_date = "2020-01-07"

        client.get_time_entries(start_date, end_date, raw=True)
        mock_get.assert_called_with(
            client.base_url + "/me/time_entries",
            auth=client.auth,
            params={
                "start_date": start_date,
                "end_date": end_date,
            },
            timeout=10,
        )
        mock_serialize.assert_not_called()

        client.get_time_entries(start_date, end_date)
        mock_serialize.assert_called_with({})

    @patch("requests.get")
    def test_serialize_time_entries(self, mock_get):
        mock_response = mock_get.return_value = Mock()
        mock_response.json.return_value = self.get_projects_side_effect()
        dummy_time_entries = [
            {
                "id": "0000000000",
                "workspace_id": "0000000",
                "project_id": "0000000",
                "task_id": None,
                "billable": False,
                "start": "2023-05-19T13:54:46+00:00",
                "stop": "2023-05-19T16:43:41Z",
                "duration": 10135,
                "description": "This is a dummy time entry",
                "tags": [],
                "tag_ids": [],
                "duronly": True,
                "at": "2023-05-19T16:43:42+00:00",
                "server_deleted_at": None,
                "user_id": "0000000",
                "uid": "0000000",
                "wid": "0000000",
                "pid": "0000000",
            },
            {
                "id": "0000000001",
                "workspace_id": "0000000",
                "project_id": "0000000",
                "task_id": None,
                "billable": False,
                "start": "2023-05-19T13:27:46+00:00",
                "stop": "2023-05-19T13:51:46Z",
                "duration": 1440,
                "description": "And another",
                "tags": [],
                "tag_ids": [],
                "duronly": True,
                "at": "2023-05-19T13:51:48+00:00",
                "server_deleted_at": None,
                "user_id": "0000000",
                "uid": "0000000",
                "wid": "0000000",
                "pid": "0000000",
            },
        ]
        client = TogglClient("token")

        serialized_time_entries = client.serialize_time_entries(
            dummy_time_entries
        )
        self.assertEqual(len(serialized_time_entries), 2)
        self.assertDictEqual(
            serialized_time_entries[0],
            {
                "description": "This is a dummy time entry",
                "duration": 10135,
                "id": "0000000000",
                "start": datetime.datetime(
                    2023, 5, 19, 13, 54, 46, tzinfo=TIMEZONE_OBJ
                ),
                "end": datetime.datetime(
                    2023, 5, 19, 16, 43, 41, tzinfo=TIMEZONE_OBJ
                ),
                "project": {
                    "client_id": "0000000",
                    "name": "Dummy Project",
                    "color": "0",
                },
            },
        )
        self.assertDictEqual(
            serialized_time_entries[1],
            {
                "description": "And another",
                "duration": 1440,
                "id": "0000000001",
                "start": datetime.datetime(
                    2023, 5, 19, 13, 27, 46, tzinfo=TIMEZONE_OBJ
                ),
                "end": datetime.datetime(
                    2023, 5, 19, 13, 51, 46, tzinfo=TIMEZONE_OBJ
                ),
                "project": {
                    "client_id": "0000000",
                    "name": "Dummy Project",
                    "color": "0",
                },
            },
        )
