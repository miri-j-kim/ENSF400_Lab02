from github import Github

# or using an access token
g = Github("token")
repo = g.get_repo("miri-j-kim/ENSF400_Lab02")

#Print all branches
print(list(repo.get_branches()))

print(repo)

#Get pull requests by query
pulls = repo.get_pulls(state='closed', sort='created', base='main')
for pr in pulls:
   print(pr)

#Task 3: List commits on main
main_branch = repo.get_branch("main")
commits = list(repo.get_commits(sha=main_branch.commit.sha))
for commit in commits:
   print(commit)
