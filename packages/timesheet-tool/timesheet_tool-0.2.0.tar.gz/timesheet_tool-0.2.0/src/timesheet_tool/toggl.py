# Standard Library
import re
from collections import OrderedDict
from datetime import datetime

# Third party
import requests

# Local
from timesheet_tool import config


class TogglClient:
    def __init__(self, token):
        self.auth = (token, "api_token")
        self.base_url = "https://api.track.toggl.com/api/v9"
        self.projects = self._get_projects()

    def _get(self, url, params={}):
        return requests.get(url, params=params, auth=self.auth, timeout=10)

    def _get_projects(self):
        response = self._get(f"{self.base_url}/me/projects")
        return {
            project["id"]: {
                "client_id": project["client_id"],
                "color": project["color"],
                "name": project["name"],
            }
            for project in response.json()
            if project.get("active")
        }

    def get_me(self):
        response = self._get(f"{self.base_url}/me")
        return response.json()

    def get_time_entries(self, start_date, end_date, raw=False):
        response = self._get(
            f"{self.base_url}/me/time_entries",
            params={
                "start_date": start_date,
                "end_date": end_date,
            },
        )

        if raw:
            return response.json()

        return self.serialize_time_entries(response.json())

    def get_project(self, project_id):
        response = self._get(f"{self.base_url}/projects/{project_id}")
        return response.json()

    def serialize_time_entries(self, time_entries):
        serialized_time_entries = []
        for entry in time_entries:
            project = self.projects[entry["project_id"]]

            serialized_time_entries.append(
                {
                    "description": entry["description"],
                    "start": datetime.strptime(
                        entry["start"], config.DATETIME_FORMAT + "+00:00"
                    ).replace(tzinfo=config.TIMEZONE_OBJ),
                    "end": datetime.strptime(
                        entry["stop"], config.DATETIME_FORMAT + "Z"
                    ).replace(tzinfo=config.TIMEZONE_OBJ),
                    "duration": entry["duration"],
                    "project": project,
                    "id": entry["id"],
                }
            )

        return serialized_time_entries


class TogglCompiler:
    def __init__(self, start_date, end_date):
        toggl_client = TogglClient(config.TOGGL_TOKEN)
        me = toggl_client.get_me()

        print(
            f"Hello {me['fullname']}\nImporting your Toggl data for last \
            week... ",
            end="",
        )
        time_entries = toggl_client.get_time_entries(start_date, end_date)
        print("Done!")

        print("Compiling your data... ", end="")
        self.compiled_time_entries = self.compile_time_entries(time_entries)
        self.final_data = self.get_final_data()
        print("Done!")

    def get_final_data(self):
        sorted_compiled_time_entries = OrderedDict(
            sorted(self.compiled_time_entries.items())
        )
        final_data = {}

        for date, projects in sorted_compiled_time_entries.items():
            final_data[date] = {}

            duration_for_day = sum(
                (
                    duration
                    for project, duration in projects.items()
                    if config.TICKET_PREFIX in project
                )
            )
            meeting_time = sum(
                (
                    duration
                    for project, duration in projects.items()
                    if config.MEETING_TICKET in project
                )
            )

            for project, duration in projects.items():
                if config.TICKET_PREFIX not in project:
                    continue

                ticket_number = re.match(config.TICKET_REGEX, project).group(0)

                if ticket_number != config.MEETING_TICKET:
                    normalized = (
                        duration
                        * (config.HOURS_IN_DAY * 3600 - meeting_time)
                        / (duration_for_day - meeting_time)
                    )

                else:
                    normalized = duration

                final_data[date][ticket_number] = (
                    self.round_hours(normalized / 3600) * 3600
                )

        return final_data

    def compile_time_entries(self, time_entries):
        compiled_time_entries = {}
        for entry in time_entries:
            date_str = entry["start"].date().strftime(config.DATE_FORMAT)
            project_name = entry["project"]["name"]

            if date_str not in compiled_time_entries:
                compiled_time_entries[date_str] = {}

            if project_name not in compiled_time_entries[date_str]:
                compiled_time_entries[date_str][project_name] = 0

            compiled_time_entries[date_str][project_name] += entry["duration"]

        return compiled_time_entries

    def print_recap_screen(self):
        print("\nHere's a recap of your week:")

        for date, projects in self.final_data.items():
            print(date)

            day_hours = 0
            for project, duration in projects.items():
                duration_in_hours = duration / 3600
                day_hours += duration / 3600

                print(f"{project:7}   {duration_in_hours:.2f} hours")

            print(f"{'':7}   {'-'*10}")
            print(f"{'':7}   {day_hours} hours\n")

    def round_hours(self, x, base=0.25):
        return base * round(x / base)
