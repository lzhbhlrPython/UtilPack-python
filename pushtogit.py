import os

def addAllToGit():
    os.system('git add .')

def commitToGit(message):
    os.system('git commit -m "'+message+'"')

def pushToGit():
    os.system('git push')

def pullFromGit():
    os.system('git pull')

def pushToGitWithMessage(message):
    addAllToGit()
    commitToGit(message)
    pushToGit()

def pullFromGitWithMessage(message):
    pullFromGit()
    addAllToGit()
    commitToGit(message)
    pushToGit()

def main():
    pushToGitWithMessage('Pushed from pushtogit.py')

if __name__ == '__main__':
    main()