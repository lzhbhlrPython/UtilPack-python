import os
import git
import time

def push_to_git():
    repo = git.Repo(os.getcwd())
    repo.git.add(update=True)
    repo.index.commit('Update at ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'.')
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == '__main__':
    push_to_git()