from github import Github

# or using an access token
g = Github("token here")
repo = g.get_repo("miri-j-kim/ENSF400_Lab02")

print(repo)

#Print all branches
print("\nTask 1 | Branches:")
branches = repo.get_branches()
for branch in branches:
   print(branch)

#Get pull requests by query
print("\nTask 2 | Pull Requests:")
pulls = repo.get_pulls(state='closed', sort='created', base='main')
for pr in pulls:
   print(pr)

#Task 3: List commits on main
print("\nTask 3 | Commits:")
main_branch = repo.get_branch("main")
commits = list(repo.get_commits(sha=main_branch.commit.sha))
for commit in commits:
   print(commit, end=': ')
   print(commit.author)
