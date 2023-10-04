from git import Repo
import os

def random_hex_string(length=6):
    return str(os.urandom(length).hex())


PATH_OF_GIT_REPO = r'J:\GH Repos\gh_commit_bot\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = random_hex_string()

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True)
        print("added")
        repo.index.commit(COMMIT_MESSAGE)
        print(f"commit {COMMIT_MESSAGE}")
        origin = repo.remote(name='origin')
        origin.push()
        print(f"pushed")
    except:
        print('Some error occured while pushing the code')    

git_push()