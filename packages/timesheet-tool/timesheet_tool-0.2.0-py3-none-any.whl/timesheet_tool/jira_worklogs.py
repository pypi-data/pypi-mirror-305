# Standard Library
from datetime import datetime, timedelta

# Third party
import config
from jira import JIRA


class JiraLoader:
    def __init__(self, toggl_data):
        self.jira = JIRA(
            config.JIRA_URL, basic_auth=(config.JIRA_EMAIL, config.JIRA_TOKEN)
        )
        self.toggl_data = toggl_data
        self.loaded_worklogs = []

    def load_worklogs(self):
        print("Loading worklogs into Jira... ", end="")

        for day, projects in self.toggl_data.items():
            date = datetime.strptime(day, config.DATE_FORMAT)
            date_time = (date + timedelta(hours=8)).replace(
                tzinfo=config.TIMEZONE_OBJ
            )

            for project, duration in projects.items():
                self.loaded_worklogs.append(
                    self.jira.add_worklog(
                        project, timeSpentSeconds=duration, started=date_time
                    )
                )

        print("Done!")

    def cancel_load(self):
        print("Cancelling worklog load... ", end="")

        for worklog in self.loaded_worklogs:
            worklog.delete(adjustEstimate="leave")

        print("Done!")
