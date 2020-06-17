from git import Repo
import DatedCommits
from datetime import datetime 


def findCommits(repo, day):

    config = repo.config_reader()
    your_email = config.get_value('user', 'email')

    heads = repo.heads
    print(len(heads))
    your_commits_in_range = []

    for head in heads:
        date = head.commit.authored_date
        author_email = head.commit.author.email
        
        commit_list = list(repo.iter_commits(head))
        # loop through commits
        print(len(commit_list))

        if author_email != your_email:
            continue
        if day == datetime.fromtimestamp(date).date():
            your_commits_in_range.append(head)
    return your_commits_in_range