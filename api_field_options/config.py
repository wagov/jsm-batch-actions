# use your own username and API token for the jira instance you are editting
USERNAME = ""
API_TOKEN = ""
BASE_JIRA_URL = ""
FIELD_ID = ""
CONTEXT_ID = ""

# e.g. r"excel_sheet/account_ids.xlsx"
OPTIONS_FILE_PATH = r""

# Don't change these
FIELD_URL = rf"/rest/api/3/field/{FIELD_ID}/context/{CONTEXT_ID}/option"
