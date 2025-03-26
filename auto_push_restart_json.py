import time, os, json, subprocess

def has_changed(file, last):
    try:
        with open(file, 'r') as f:
            current = json.load(f)
            return current != last, current
    except:
        return False, last

if __name__ == "__main__":
    last_json = {}
    while True:
        changed, new_data = has_changed("restart-time.json", last_json)
        if changed:
            print("Changes detected. Pushing to GitHub...")
            subprocess.call(["git", "add", "restart-time.json"])
            subprocess.call(["git", "commit", "-m", "Auto update"])
            subprocess.call(["git", "push"])
            last_json = new_data
        time.sleep(60)
