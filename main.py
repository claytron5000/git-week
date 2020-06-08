import core


repoPath = "../../Projects/barnard"
start_date = 1587581435
end_date = 1591368032


commits = core.findCommits(repoPath, start_date, end_date)

print(len(commits))