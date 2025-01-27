from github import Github

# or using an access token
g = Github("your_access_token")
repo = g.get_repo("miri-j-kim/ENSF400_Lab02")

list(repo.get_branches())

print(repo)
