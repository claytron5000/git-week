from os import listdir
from os.path import isdir, join
from git import Repo


def getGitDirectories(top_dir):
    repos =[]
    only_dir = [join(top_dir, d) for d in listdir(top_dir) if isdir(join(top_dir, d))]
    for repo_path in only_dir:
        has_git = False
        for entry in listdir(repo_path):
            if (entry == ".git"): 
                has_git = True
                break
        if(has_git): 
            repo = Repo(repo_path) 
            assert not repo.bare
            repos.append(repo)


    return repos
