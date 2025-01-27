from github import Github

# or using an access token
g = Github("your_access_token")
repo = g.get_repo("miri-j-kim/ENSF400_Lab02")

#Print all branches
print(list(repo.get_branches()))

print(repo)

#Get pull requests by number
pr = repo.get_pull(664)
pr

#Get pull requests by query
pulls = repo.get_pulls(state='open', sort='created', base='master')
for pr in pulls:
   print(pr.number)

#Task 3: List commits on main
main_branch = repo.get_branch("main")
commits = list(repo.get_commits(sha=main_branch.commit.sha))
print(commits)
