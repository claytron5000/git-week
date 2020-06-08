import core
import directories
from datetime import timedelta, datetime
from DateRange import DateRange
from DatedCommits import DatedCommits
from dates import getLastWeek

# repoPath = "../../Projects"
# start_date = 1587581435
# end_date = 1591368032
# date_range =  DateRange(start_date, end_date)

# def findMyCommitsInDates(repo_path):
#     repos = directories.getGitDirectories(repo_path)
#     dated_commits = []
#     for repo in repos: 
#         commits = core.findCommits(repo, date_range)
#         if len(commits) > 0 : 
#             dated_commit = DatedCommits(repo, date_range, commits)
#             dated_commits.append(dated_commit)

#     return dated_commits


def loopThroughDates():
    repos = directories.getGitDirectories("../../Projects")
    curr_day = getLastWeek()
    last_sunday = curr_day + timedelta(weeks=1)
    delta = timedelta(days=1)
    while curr_day < last_sunday:
        print(curr_day.strftime("%A"))
        for repo in repos: 
            commits = core.findCommits(repo, curr_day)
            if len(commits) > 0 : 
                # todo use the datedcommits to do printing/ layout
                # dated_commit = DatedCommits(repo, curr_day, commits)
                print("\t", repo.working_dir[repo.working_dir.rindex("/")+1:].capitalize())
                for head in commits:
                    print("\t\t", datetime.fromtimestamp(head.commit.authored_date).time().strftime("%I:%M%p"))
                    print("\t\t", head.commit.summary)
                    print("\t\t", head.commit.size)
                
        curr_day += delta


loopThroughDates()