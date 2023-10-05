from git import Repo
from os import urandom
import random
import time
from datetime import datetime

def random_hex_string(length=6):
    return str(urandom(length).hex())

def git_add_commit_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True)
        print("[*] git add .")
        repo.index.commit(COMMIT_MESSAGE)
        print(f"[*] git commit -m {COMMIT_MESSAGE}")
        origin = repo.remote(name='origin')
        origin.push()
        print(f"[*] git push -u origin main\n")
    except:
        print('[!] Error in git_add_commit_push()\n\n')    

PATH_OF_GIT_REPO = r'J:\GH Repos\gh_commit_bot\.git'  # make sure .git folder is properly configured

run_id = random.choice(range(1,100000))     # used to identify a particular run in the log file. 

max_loop = 100

for run in range(max_loop):      
    try:
        
        COMMIT_MESSAGE = random_hex_string()

        # make a timestamp for this run, and print message
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH commit bot: commit:{COMMIT_MESSAGE}, run:{run}, max_loop:{max_loop}, run_id:{run_id}  [{start_timestamp_str}]")


        # with open(f"{local_dir}/{update_file}", "a") as f:
#           f.write("\nUpdate version 2")

        with open(f"output\\commits.txt", 'a') as f:
            f.write(f"{COMMIT_MESSAGE}\n")

        time.sleep(1)

        git_add_commit_push()

        with open(f"log_files\GITHUB_BOT_{current_date}_{run_id}.txt", 'a') as f:
            f.write(f"[COMMIT:{COMMIT_MESSAGE}] [run:{run}] [Start:{start_timestamp_str}] [max_loop:{max_loop}] [run_id:{run_id}]\n\n")

        
        # log = open(f"log_files\GITHUB_BOT_{current_date}_{run_id}.txt", 'a')
        # log.write(f"[run:{run}] [new profile view count:{count}] [Start:{start_timestamp_str}] [max_loop:{max_loop}] [run_id:{run_id}]\n\n")
        # log.close()

        time.sleep(3)
    
    except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
        print(f"[!] GH commit bot exited at run: {run}")
        break

