import json
from config import *
from api import Api
import time


def get_issue_list():
    index = 0
    issue_list = []

    if len(JQL_SEARCH) < 12:  # ensure JQL is at least as long as 'project = x'
        raise Exception("JQL must be at least 12 characters in length.")
    response = search_issues(index)
    if response.get('errorMessages'):
        raise Exception(f"Error with issue search - {response.get('errorMessages')}")
    max_results = response['maxResults']
    total = response['total']
    issue_list.extend([issue['key'] for issue in response['issues']])

    while index + max_results < total:
        index = index + max_results
        response = search_issues(index)
        issue_list.extend([issue['key'] for issue in response['issues']])

    return issue_list


def search_issues(i):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    body = {
        "jql": JQL_SEARCH,
        "maxResults": 10000,
        "startAt": i
    }

    return Api.post_request(BASE_JIRA_URL + SEARCH_ISSUE_URL, headers, json.dumps(body))


def delete_issues(issues):
    count = 0
    for issue in issues:
        response = Api.delete_request(BASE_JIRA_URL + DELETE_ISSUE_URL + issue, '')
        if response.get('errorMessages'):
            raise Exception(f"Error with issue deletion - {response.get('errorMessages')} - {issue}")
        count = count + 1
        if count % 100 == 0:
            print(f"{count} issues deleted")


if __name__ == '__main__':
    issues_to_delete = []
    try:
        start = time.time()
        issues_to_delete = get_issue_list()
        end = time.time()
        print(f"The time of execution of issue search is : {(end - start)} s for {len(issues_to_delete)} issues")
    except Exception as e:
        print(f"Error with issue search - {str(e)}")

    if len(issues_to_delete) > 0:
        try:
            start = time.time()
            delete_issues(issues_to_delete)
            end = time.time()
            print("The time of execution of issue deletion is :",
                  (end - start), "s")
        except Exception as e:
            print(f"Error with deletion - {str(e)}")
    else:
        print("No issues to delete")
