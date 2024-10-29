# Standard Library
import os

# Third party
import pytz
from dotenv import load_dotenv

load_dotenv()


TOGGL_TOKEN = os.environ.get("TOGGL_TOKEN")
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIMEZONE = "America/New_York"
TIMEZONE_OBJ = pytz.timezone(TIMEZONE)
TICKET_PREFIX = os.environ.get("TICKET_PREFIX")
TICKET_REGEX = f"{TICKET_PREFIX}-[0-9]*"
HOURS_IN_DAY = float(os.environ.get("HOURS_IN_DAY"))
MEETING_TICKET = os.environ.get("MEETING_TICKET")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")
JIRA_URL = os.environ.get("JIRA_URL")
