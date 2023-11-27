# github commit bot

from git import Repo
from os import urandom
from datetime import datetime
import random
import time
import requests


def random_hex_string(length=3):
    return str(urandom(length).hex())

def git_add_commit_push(COMMIT_MESSAGE):
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        origin = repo.remote(name='origin')
        
        repo.git.add(all=True)
        print("[*] git add .")
        repo.index.commit(COMMIT_MESSAGE)
        print(f"[*] git commit -m {COMMIT_MESSAGE}")
        origin.push()
        print(f"[*] git push -u origin main\n")
    except:
        print('[!] Error in git_add_commit_push()\n\n')    

PATH_OF_GIT_REPO = r'J:\GH Repos\gh_commit_bot\.git'  # make sure .git folder is properly configured

run_id = random_hex_string     # used to identify a particular run in the log file. 

current_commits_url = "https://camo.githubusercontent.com/372ebfb40b1316d44bf6914d6134178c9ec06d92dd1265788a21c4074ec158c7/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d6a726f6c6c6572333326"

response = requests.get(current_commits_url)
current_commits = response.text.splitlines()[35].strip()

max_loop = int(input(f"\nCurrent github commits: {current_commits}.\nHow many times do you want to run the GH commit bot? "))


for run in range(max_loop):      
    try:
        COMMIT_MESSAGE = random_hex_string()

        # make a timestamp for this run, and print message
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH commit bot: run:{run}, max_loop:{max_loop}, run_id:{run_id}  [{start_timestamp_str}]")

        with open(f"log_files\GITHUB_BOT_{current_date}.txt", 'a') as f:
            f.write(f"COMMIT_MESSAGE: [run_id:{run_id}] [Ran {run} times] [Start:{start_timestamp_str}] [max_loop:{max_loop}]\n\n")

        time.sleep(1)

        git_add_commit_push(COMMIT_MESSAGE)

        time.sleep(3)
    
    except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
        print(f"[!] GH commit bot exited at run: {run}")
        break
