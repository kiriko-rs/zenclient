import sys
sys.path.append('../zenmod')

from zenmod.zenclient import ZenClient,InvalidRequestError,UnexpectedResponseError
import requests
import pytest

def test_get_single_issue_200(requests_mock):
    host = 'https://api.zenhub.com'
    repo_id = '267155344'
    issue_number = '2'
    client = ZenClient(repo_id=repo_id)
    requests_mock.get(f'{host}/p1/repositories/{repo_id}/issues/{issue_number}', status_code=200, json={'result':'success'})
    r = client.get_single_issue(issue_number=2)
    assert r.status_code == 200
    assert r.json()['result'] == 'success'

def test_get_single_issue_401(requests_mock):
    host = 'https://api.zenhub.com'
    repo_id = '267155344'
    issue_number = '2'
    client = ZenClient(repo_id=repo_id)
    requests_mock.get(f'{host}/p1/repositories/{repo_id}/issues/{issue_number}', status_code=401)
    with pytest.raises(InvalidRequestError):
        client.get_single_issue(issue_number=2)
def test_get_single_issue_403(requests_mock):
    host = 'https://api.zenhub.com'
    repo_id = '267155344'
    issue_number = '2'
    client = ZenClient(repo_id=repo_id)
    requests_mock.get(f'{host}/p1/repositories/{repo_id}/issues/{issue_number}', status_code=403)
    with pytest.raises(InvalidRequestError):
        client.get_single_issue(issue_number=2)

def test_get_single_issue_404(requests_mock):
    host = 'https://api.zenhub.com'
    repo_id = '267155344'
    issue_number = '2'
    client = ZenClient(repo_id=repo_id)
    requests_mock.get(f'{host}/p1/repositories/{repo_id}/issues/{issue_number}', status_code=404)
    with pytest.raises(InvalidRequestError):
        client.get_single_issue(issue_number=2)

def test_get_single_issue_500(requests_mock):
    host = 'https://api.zenhub.com'
    repo_id = '267155344'
    issue_number = '2'
    client = ZenClient(repo_id=repo_id)
    requests_mock.get(f'{host}/p1/repositories/{repo_id}/issues/{issue_number}', status_code=500)
    with pytest.raises(UnexpectedResponseError):
        client.get_single_issue(issue_number=2)