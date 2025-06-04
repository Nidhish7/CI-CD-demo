import subprocess

def run_lint():
    print("Running pylint...")
    subprocess.run(["pylint", "app"], check=True)

def run_tests():
    print("Running pytest...")
    subprocess.run(["pytest", "tests"], check=True)
    
if __name__ == "__main__":
    run_lint()
    run_tests