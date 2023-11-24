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
        string = f"[{time}] {RED}[ERROR] {msg}{RESET}"
        print(string)
        return string.replace(RED, "").replace(RESET, "") + "\n"
    elif lvl == "WARN":
        string = f"[{time}] {YELLOW}[WARNING] {msg}{RESET}"
        print(string)
        return string.replace(YELLOW, "").replace(RESET, "") + "\n"
    elif lvl == "INFO":
        string = f"[{time}] {BLUE}[INFO] {msg}{RESET}"
        print(string)
        return string.replace(BLUE, "").replace(RESET, "") + "\n"
    elif lvl == "DEBUG":
        string = f"[{time}] {PURPLE}[DEBUG] {msg}{RESET}"
        print(string)
        return string.replace(PURPLE, "").replace(RESET, "") + "\n"
    else:
        string = f"[{time}] [{lvl}] {msg}"
        print(string)
        return string + "\n"
   
# This might be removed in the future
def logtofile(strawlog):
       with open("logs.txt", "a") as f:
           f.write(strawlog)
