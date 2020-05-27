import requests
import os

class ZenClient(object):
    def __init__(self, repo_id:int):
        self.token = os.getenv('ZENHUB_API')
        self.host = 'https://api.zenhub.com'
        self.repo_id = repo_id
    def get_single_issue(self, issue_number:int):
        headers = {}
        headers['X-Authentication-Token'] = self.token
        headers['Content-Type'] = 'application/json'
        url = f'{self.host}/p1/repositories/{self.repo_id}/issues/{issue_number}'
        print(url)
        r = requests.get(url=url,headers=headers)
        print(r)
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

class InvalidRequestError(Exception):
    pass
class UnexpectedResponseError(Exception):
    pass