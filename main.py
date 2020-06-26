import core
import directories
from datetime import timedelta, datetime
from itertools import repeat
from fabulous.color import bold, highlight_cyan, magenta
from pathlib import Path
from git import Repo



from DateRange import DateRange
from DatedCommits import DatedCommits
from dates import getLastWeek
from DiffDisplay import DiffDisplay
from RepoFilter import RepoFilter



def loopThroughDates(*,projects_path, start_date, end_date):
    # repos = directories.getGitDirectories("../../Playground")
    curr_day = start_date #getLastWeek()
    # last_sunday = start_date #curr_day + timedelta(weeks=1)
    delta = timedelta(days=1)

    while curr_day <= end_date:

        # Print the Day header
        day_name = curr_day.strftime("%A")
        hr = ''.join(list(repeat("-", 40-(len(day_name)//2))))
        print("\n", bold(hr + " " + day_name + " " + hr))

        for path in projects_path.iterdir():
            repo_path = path / ".git"
            if(not repo_path.exists() or not repo_path.is_dir):
                continue
            # if (repo.is_dir() and Path(repo+"/.git")):
            repo = Repo(repo_path)
            repoFilter = RepoFilter(repo)
            repoFilter.getCommitsInDay(curr_day)


                
        curr_day += delta


# loopThroughDates()