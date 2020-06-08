from git import Repo


def findCommits(repoPath, start_date, end_date):

    repo = Repo(repoPath) 
    assert not repo.bare

    config = repo.config_reader()
    your_email = config.get_value('user', 'email')

    heads = repo.heads

    your_commits_in_range = []

    for x in heads:
        date = x.commit.authored_date
        author_email = x.commit.author.email
        
        if author_email != your_email:
            continue
        if date > start_date and date < end_date:
            your_commits_in_range.append(x)
            # print(x.commit.authored_date)
            # print(x.commit.summary)
    return your_commits_in_range