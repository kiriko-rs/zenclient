import os
from zenmod.zenclient import ZenClient
from github import Github
from sheet.sheet_client import SheetClient

SHEET_ID='1Tke68dAxtJ91k1LT9rV7C639_sC3VmVm2H8PyjWJDt0'

if __name__ == '__main__':
    # エクセルデータを取ってくる
    sheet_client = SheetClient(sheet_id=SHEET_ID)
    nepics = sheet_client.getIssuesFromSheet(sheet_range='epic!A2:H24')
    nissues = sheet_client.getIssuesFromSheet(sheet_range='issues!A2:H24')
    # 以下ループ
    gclient = Github(os.environ.get('GITHUB_TOKEN'))
    zclient = ZenClient(repo_id='267511792',workspace_id='-5ecf5abec33421dcd3252f50')
    for n in nepics:
        repo = gclient.get_repo(n.repository)
        oissues = repo.get_issues()
        if len(list(filter(lambda o: o.title == n.title, oissues))) == 0:
            milestone = repo.get_milestone(number=n.milestone)
            result = repo.create_issue(title=n.title,body=n.body,assignee=n.assignee,milestone=milestone,labels=n.labels)
            print(result.number)
            print(result.repository.id)
            zclient.convert_to_epic(repo_id=result.repository.id, issue_number=result.number)
    content = {"add_issues": [],"remove_issues": []}
    for i in nissues:
        repo = gclient.get_repo(i.repository)
        oissues = repo.get_issues()
        result = None
        if len(list(filter(lambda o: o.title == i.title, oissues))) == 0:
            milestone = repo.get_milestone(number=i.milestone)
            result = repo.create_issue(title=i.title,body=i.body,assignee=i.assignee,milestone=milestone,labels=i.labels)