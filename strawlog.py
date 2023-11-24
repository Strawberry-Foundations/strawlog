import datetime

time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Color formatting
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;36m"
PURPLE = "\033[1;35m"
RESET = "\033[0;0m"

def strawlog(msg, lvl):
    if lvl == "ERROR":
        print(f"[{time}] {RED}[ERROR] {msg}{RESET}")
        return f"[{time}] {RED}[ERROR] {msg}{RESET}"
    elif lvl == "WARN":
        print(f"[{time}] {YELLOW}[WARNING] {msg}{RESET}")
        return f"[{time}] {YELLOW}[WARNING] {msg}{RESET}"
    elif lvl == "DEBUG":
        print(f"[{time}] {PURPLE}[DEBUG] {msg}{RESET}")
        return f"[{time}] {PURPLE}[DEBUG] {msg}{RESET}"
    elif lvl == "INFO":
        print(f"[{time}] {BLUE}[INFO] {msg}{RESET}")
        return f"[{time}] {BLUE}[INFO] {msg}{RESET}"
    else:
        print(f"[{time}] [{lvl}] {msg}")
        return f"[{time}] [{lvl}] {msg}"
   
# This might be removed in the future
def logtofile(strawlog):
       with open("logs.txt", "a") as f:
           f.write(strawlog)
