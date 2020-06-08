from git import Repo
import DatedCommits


def findCommits(repo, date_range):

    config = repo.config_reader()
    your_email = config.get_value('user', 'email')

    heads = repo.heads

    your_commits_in_range = []

    for head in heads:
        date = head.commit.authored_date
        author_email = head.commit.author.email
        
        if author_email != your_email:
            continue
        if date > date_range.start and date < date_range.end:
            your_commits_in_range.append(head)
            # print(head.commit.authored_date)
            # print(head.commit.summary)
    return your_commits_in_range