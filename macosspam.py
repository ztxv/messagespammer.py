# THIS SCRIPT WAS MADE ON
# M1 MacBook Air, 2020

import subprocess
import time

def send_message(message, repeat, delay):
    for _ in range(repeat):
        subprocess.run(["osascript", "-e", f'tell application "System Events" to keystroke "{message}"'])
        time.sleep(delay)

def setup():
    message = input("What message would you like to send?: ")
    repeat = int(input("How many times would you like to send it?: "))
    delay = float(input("How fast would you like the message (in seconds)?: "))
    
    print(f"Waiting for 5 seconds before starting...")
    time.sleep(5)
    
    send_message(message, repeat, delay)

if __name__ == "__main__":
    setup()
