import sys
sys.dont_write_bytecode = True

from zenmod.zenclient import ZenClient
if __name__ == '__main__':
    print(ZenClient(repo_id=267155344).get_single_issue(issue_number=1).json())