import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')


def git_status():
    print("\nChecking the git status...")
    try:
        subprocess.run(["git", "status"])
    except subprocess.CalledProcessError:
        print("\n❌ Failed to check Git Status.")
        
        
def git_add():
    print("\nAdding to git...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        print("\n✅ Added the local files to git")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to add files")
        
        
def has_changes_to_commit():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        print(f"Git status --porcelain output:\n{result.stdout!r}")  #debug print
        return result.stdout.strip() != ""
    except subprocess.CalledProcessError:
        print("\n❌ Failed to check the changes.")
        return False
    
    
def git_commit(message):
    print("\nCommitting the changes...")
    try:
        subprocess.run(["git", "commit", "-m", message], check=True)
        print("\n✅ Successfully committed the changes")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to commit the changes.")
    
    
def git_push(first_push = True):
    print("\nPushing the changes the GitHub...")
    try:
        if first_push:
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            print("\n✅ Successfully pushed the changes to Github")
        else:
            subprocess.run(["git", "push"], check=True)
            print("\n✅ Successfully pushed the changes to Github")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to push the changes.")



#------------------------------ Main Execution ------------------------------#

if __name__ == "__main__":
    
    try:
        git_status()

        if has_changes_to_commit():
            git_add()
            message = input("\nEnter the commit message you would like to proceed with: ")
            git_commit(message)
            git_push()
        else:
            print("\n✅ No Changes to commit.")
    except Exception as e:
        print(f"🚨Unexpected error: {e}")
        