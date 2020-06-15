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



def loopThroughDates(*,projects_path, start_date, end_date):
    # repos = directories.getGitDirectories("../../Playground")
    curr_day = getLastWeek()
    last_sunday = curr_day + timedelta(weeks=1)
    delta = timedelta(days=1)

    while curr_day < last_sunday:

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
            commits = core.findCommits(repo, curr_day)
            if len(commits) > 0 : 
                # todo use the datedcommits to do printing/ layout
                print("\t", bold(repo.working_dir[repo.working_dir.rindex("/")+1:].capitalize()))
                for head in commits:
                    print("\t\t" + bold("- ") + head.commit.summary, "(" + datetime.fromtimestamp(head.commit.authored_date).time().strftime("%I:%M%p")+")")
                    # print("\t\t", )
                    if len(head.commit.parents) == 1:
                        parent = head.commit.parents[0]
                        diff_string = repo.git.diff(head.commit, parent, shortstat=True)
                        diffDisplay = DiffDisplay(diff_string)
                        diffDisplay.print()
                
        curr_day += delta


# loopThroughDates()