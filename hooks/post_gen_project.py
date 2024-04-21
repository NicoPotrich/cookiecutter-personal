import subprocess

user = input("Do you want to create a GIT repository?([y]/n)" ).strip().lower() or "y"

if user == "y":
    MESSAGE_COLOR = "\x1b[34m"
    RESET_ALL = "\x1b[0m"

    print(f"{MESSAGE_COLOR}Almost done!")
    print(f"Initializing a git repository...{RESET_ALL}")

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])

    print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")

else:
    print("No problem! You can always initialize a git repository later if you change your mind. Enjoy creating your project!")



