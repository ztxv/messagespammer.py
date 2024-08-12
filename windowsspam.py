import time
import pyautogui

def send_message(message, repeat, delay):
    for _ in range(repeat):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(delay)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i}")
        time.sleep(1)

def setup():
    start_time = time.time()
    print("\n ")
    message = input("What message would you like to send?: ")
    repeat = int(input("How many times would you like to send it?: "))
    delay = float(input("How fast would you like the message (in seconds)?: "))
    countdown_seconds = int(input("Input how many seconds until bot starts: "))

    print(f"{countdown_seconds} seconds until bot starts...")

    countdown(countdown_seconds)

    send_message(message, repeat, delay)

    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time
    print("FINISHED")
    print(f"Total time taken: {total_time:.2f} seconds")

    # Count the number of words and letters in the message
    num_words = len(message.split())
    num_letters = sum(c.isalpha() for c in message)
    total_words_sent = repeat * num_words
    total_letters_sent = repeat * num_letters

    print(f"Total words sent: {total_words_sent}")
    print(f"Total letters sent: {total_letters_sent}")

setup()
