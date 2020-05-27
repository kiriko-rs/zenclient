import sys
sys.path.append('../zenmod')

from zenmod.zenclient import ZenClient,InvalidRequestError,UnexpectedResponseError
import requests
import pytest


class TestZenclient:
    _host = 'https://api.zenhub.com'
    _repo_id = '267155344'
    _workspace_id = '5ecd8973acce48539648a593'
    _issue_number = '1'
    _client = ZenClient(repo_id=_repo_id, workspace_id=_workspace_id)

    '''
    issue取得メソッド単体テスト
    '''
    def test_get_single_issue_200_unmocked(self):
        r = self._client.get_single_issue(issue_number=self._issue_number)
        assert r.status_code == 200 
        assert r.json()['is_epic'] == False

    def test_get_single_issue_200(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}', status_code=200, json={"test_get_single_issue_200":"ok"})
        r = self._client.get_single_issue(issue_number=self._issue_number)
        assert r.status_code == 200 
        assert r.json()['test_get_single_issue_200'] == "ok"

    def test_get_single_issue_401(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}', status_code=401)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue(issue_number=self._issue_number)

    def test_get_single_issue_403(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}', status_code=403)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue(issue_number=self._issue_number)

    def test_get_single_issue_404(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}', status_code=404)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue(issue_number=self._issue_number)

    def test_get_single_issue_500(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}', status_code=500)
        with pytest.raises(UnexpectedResponseError):
            self._client.get_single_issue(issue_number=self._issue_number)

    '''
    イベント取得メソッド単体テスト
    '''
    def test_get_single_issue_events_200_unmocked(self):
        r = self._client.get_single_issue_events(issue_number=self._issue_number)
        assert r.status_code == 200 

    def test_get_single_issue_events_200(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}/events', status_code=200, json={"test_get_single_issue_200":"ok"})
        r = self._client.get_single_issue_events(issue_number=self._issue_number)
        assert r.status_code == 200 
        assert r.json()['test_get_single_issue_200'] == "ok"

    def test_get_single_issue_events_401(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}/events', status_code=401)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue_events(issue_number=self._issue_number)

    def test_get_single_issue_events_403(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}/events', status_code=403)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue_events(issue_number=self._issue_number)

    def test_get_single_issue_events_404(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}/events', status_code=404)
        with pytest.raises(InvalidRequestError):
            self._client.get_single_issue_events(issue_number=self._issue_number)

    def test_get_single_issue_events_500(self, requests_mock):
        requests_mock.get(f'{self._host}/p1/repositories/{self._repo_id}/issues/{self._issue_number}/events', status_code=500)
        with pytest.raises(UnexpectedResponseError):
            self._client.get_single_issue_events(issue_number=self._issue_number)

    '''
    パイプライン移動メソッド単体テスト
    '''
    def test_post_single_issue_moves_200(self, requests_mock):
        json={"pipeline_id": "58bf13aba426771426665e60","position": "Icebox"}
        requests_mock.post(f'{self._host}/p2/workspaces/{self._workspace_id}/repositories/{self._repo_id}/issues/{self._issue_number}/moves', status_code=200, json={"test_post_single_issue_200":"ok"})
        r = self._client.post_single_issue_moves(issue_number=self._issue_number,workspace_id=self._workspace_id, json=json)
        assert r.status_code == 200 
        assert r.json()['test_post_single_issue_200'] == "ok"

    def test_post_single_issue_moves_401(self, requests_mock):
        json={"pipeline_id": "58bf13aba426771426665e60","position": "bottom"}
        requests_mock.post(f'{self._host}/p2/workspaces/{self._workspace_id}/repositories/{self._repo_id}/issues/{self._issue_number}/moves', status_code=401)
        with pytest.raises(InvalidRequestError):
            self._client.post_single_issue_moves(issue_number=self._issue_number,workspace_id=self._workspace_id, json=json)

    def test_post_single_issue_moves_403(self, requests_mock):
        json={"pipeline_id": "58bf13aba426771426665e60","position": "top"}
        requests_mock.post(f'{self._host}/p2/workspaces/{self._workspace_id}/repositories/{self._repo_id}/issues/{self._issue_number}/moves', status_code=403)
        with pytest.raises(InvalidRequestError):
            self._client.post_single_issue_moves(issue_number=self._issue_number,workspace_id=self._workspace_id, json=json)

    def test_post_single_issue_moves_404(self, requests_mock):
        json={"pipeline_id": "58bf13aba426771426665e60","position": "top"}
        requests_mock.post(f'{self._host}/p2/workspaces/{self._workspace_id}/repositories/{self._repo_id}/issues/{self._issue_number}/moves', status_code=404)
        with pytest.raises(InvalidRequestError):
            self._client.post_single_issue_moves(issue_number=self._issue_number,workspace_id=self._workspace_id, json=json)

    def test_post_single_issue_moves_500(self, requests_mock):
        json={"pipeline_id": "58bf13aba426771426665e60","position": "top"}
        requests_mock.post(f'{self._host}/p2/workspaces/{self._workspace_id}/repositories/{self._repo_id}/issues/{self._issue_number}/moves', status_code=500)
        with pytest.raises(UnexpectedResponseError):
            self._client.post_single_issue_moves(issue_number=self._issue_number,workspace_id=self._workspace_id, json=json)