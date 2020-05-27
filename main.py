import sys
sys.dont_write_bytecode = True

import zenclient.zenclient as zenclient
if __name__ == '__main__':
    zenclient.ZenClient(repo_id=267155344).get_single_issue(issue_number=1)