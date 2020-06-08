import core
import directories
from DateRange import DateRange
from DatedCommits import DatedCommits

repoPath = "../../Projects"
start_date = 1587581435
end_date = 1591368032
date_range =  DateRange(start_date, end_date)

def findMyCommitsInDates(repo_path):
    repos = directories.getGitDirectories(repo_path)
    dated_commits = []
    for repo in repos: 
        commits = core.findCommits(repo, date_range)
        if len(commits) > 0 : 
            dated_commit = DatedCommits(repo, date_range, commits)
            dated_commits.append(dated_commit)

    return dated_commits

print(findMyCommitsInDates(repoPath))