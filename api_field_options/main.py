import json
import pandas as pd
from config import *
from api import Api


def post_create_options(opts):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    body = {"options": [{
      "disabled": False,
      "value": o
    } for o in opts]}

    Api.post_request(BASE_JIRA_URL + FIELD_URL, headers, json.dumps(body))


if __name__ == '__main__':
    df = pd.read_excel(OPTIONS_FILE_PATH)
    field_options = df.iloc[:, df.shape[1] - 1].to_list()

    post_create_options(field_options)

    print("all done :)")
