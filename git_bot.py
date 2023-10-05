from git import Repo
from os import urandom
import random
import time
from datetime import datetime

def random_hex_string(length=6):
    return str(urandom(length).hex())


PATH_OF_GIT_REPO = r'J:\GH Repos\gh_commit_bot\.git'  # make sure .git folder is properly configured

def git_add_commit_push():
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

# git_push()


run_id = random.choice(range(1,100000))     # used to identify a particular run in the log file. 

max_loop = 5

for run in range(max_loop):      
    try:
        
        COMMIT_MESSAGE = random_hex_string()

        # make a timestamp for this run, and print message
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH commit bot run at run:{run}, max_loop:{max_loop}, run_id:{run_id} commit:{COMMIT_MESSAGE} [{start_timestamp_str}]")


        # with open(f"{local_dir}/{update_file}", "a") as f:
#           f.write("\nUpdate version 2")

        with open(f"output\\commits.txt", 'a') as f:
            f.write(f"{COMMIT_MESSAGE}\n")

        time.sleep(1)

        git_add_commit_push()
        # file = open(f"output\\commits.txt", 'a')
        # file.write(f"{COMMIT_MESSAGE}\n")
        # file.close()

        time.sleep(2)
    
    except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
        print(f"[!] GH commit bot exited at run: {run}")
        break