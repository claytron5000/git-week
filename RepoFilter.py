from git import Repo
from datetime import timedelta, datetime

class RepoFilter:

    def __init__(self, repo):
        self.repo = repo
        self.commits = {}
        self.heads= list(repo.heads)

    def getCommitsInDay(self, day):
        self.current_day = day
        for head in self.heads:
            self.commits[head] = self.__gatherCommits(head)
    
    def __gatherCommits(self, head, count=2, commits=[]):
        next_commits = list(self.repo.iter_commits(head, max_count=count))
        last_commit = next_commits[len(next_commits)-1].committed_date
        filtered_commits = list(filter(lambda x: x.committed_date == self.current_day, next_commits))
        commits += next_commits

        if last_commit == self.current_day:
            return self.__gatherCommits(head, count*2, commits)
        else:
            return commits

    def print():
        for head in commits:
            print("head: ")
            print(head)
