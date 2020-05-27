import requests
import os

def checkResponse(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        if(r.status_code == 401):
            raise InvalidRequestError(f'The token is not valid. See Authentication.https://github.com/ZenHubIO/API#authentication\nresponse: {r}')
        elif(r.status_code == 403):
            raise InvalidRequestError(f'Reached request limit to the API. See API Limits.https://github.com/ZenHubIO/API#api-rate-limits\nresponse: {r}')
        elif(r.status_code == 404):
            raise InvalidRequestError(f'Not found.\nresponse: {r}')
        elif(r.status_code == 200):
            return r
        else:
           raise UnexpectedResponseError('unexpected response.') 
    return wrapper

class ZenClient(object):
    def __init__(self, repo_id:int, workspace_id:str):
        self.host = 'https://api.zenhub.com'
        self.repo_id = repo_id
        self.workspace_id = workspace_id
        self.headers =  {}
        self.headers['X-Authentication-Token'] = os.getenv('ZENHUB_TOKEN')
        self.headers['Content-Type'] = 'application/json'

    @checkResponse
    def get_single_issue(self, issue_number:int):
        url = f'{self.host}/p1/repositories/{self.repo_id}/issues/{issue_number}'
        return requests.get(url=url,headers=self.headers)
    
    @checkResponse
    def get_single_issue_events(self, issue_number:int):
        url = f'{self.host}/p1/repositories/{self.repo_id}/issues/{issue_number}/events'
        return requests.get(url=url,headers=self.headers)

    @checkResponse
    def post_single_issue_moves(self, workspace_id:str, issue_number:int, json:dict):
        url = f'{self.host}/p2/workspaces/{workspace_id}/repositories/{self.repo_id}/issues/{issue_number}/moves'
        return requests.post(url=url,headers=self.headers,data=json)
    
    @checkResponse
    def put_single_issue_estimate(self, workspace_id:str, issue_number:int, json:dict):
        url = f'{self.host}/p2/workspaces/{workspace_id}/repositories/{self.repo_id}/issues/{issue_number}/moves'
        return requests.post(url=url,headers=self.headers,data=json)

class InvalidRequestError(Exception):
    pass
class UnexpectedResponseError(Exception):
    pass