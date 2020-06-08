class DatedCommits:
    def __init__(self, repo, date_range, commits):
        self.repo = repo
        self.date_range = date_range
        self.commits = commits