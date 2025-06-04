import subprocess

def git_status():
    print("Checking the git status...")
    try:
        subprocess.run(["git", "status"])
    except subprocess.CalledProcessError:
        print("Failed to check Git Status.")
        
        
def git_add():
    print("Adding to git...")
    try:
        subprocess.run(["git", "add", "."], check=True)
    except subprocess.CalledProcessError:
        print("Failed to add files")
        
        
def has_changes_to_commit():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        print(f"Git status --porcelain output:\n{result.stdout!r}")  #debug print
        return result.stdout.strip() != ""
    except subprocess.CalledProcessError:
        print("Failed to check the changes.")
        return False
    
    
def git_commit(message):
    print("Committing the changes...")
    try:
        subprocess.run(["git", "commit", "-m", message], check=True)
    except subprocess.CalledProcessError:
        print("Failed to commit the changes.")
    
    
def git_push(first_push = True):
    print("Pushing the changes the GitHub...")
    try:
        if first_push:
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            print("Successfully pushed the changes to Github")
        else:
            subprocess.run(["git", "push"], check=True)
            print("Successfully pushed the changes to Github")
    except subprocess.CalledProcessError:
        print("Failed to push the changes.")



#------------------------------ Main Execution ------------------------------#

if __name__ == "__main__":
    
    git_status()

    if has_changes_to_commit():
        git_add()
        message = input("Enter the commit message you would like to proceed with.")
        git_commit(message)
        git_push()
    else:
        print("No Changes to commit.")
        