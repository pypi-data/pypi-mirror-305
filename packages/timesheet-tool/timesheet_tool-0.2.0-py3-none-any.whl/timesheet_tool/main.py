# Standard Library
import argparse

# Third party
from jira_worklogs import JiraLoader
from toggl import TogglCompiler


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s",
        "--start-date",
        help="Start date for the report",
        required=True,
    )
    parser.add_argument(
        "-e",
        "--end-date",
        help="End date for the report",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--test",
        help="Is this a test run?",
        action=argparse.BooleanOptionalAction,
    )

    return vars(parser.parse_args())


if __name__ == "__main__":
    args = get_args()
    test = args.pop("test", False)

    toggl_compiler = TogglCompiler(**args)
    toggl_compiler.print_recap_screen()

    jira_loader = JiraLoader(toggl_compiler.final_data)
    if input("Do you want to load worklogs into Jira? [y/n] ") == "y":
        if not test:
            jira_loader.load_worklogs()

            if input("Cancel last action? [y/n] ") == "y":
                jira_loader.cancel_load()

        else:
            print("Skipping loading worklogs into Jira")
