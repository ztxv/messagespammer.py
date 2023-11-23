import time
import subprocess

def send_message(message, repeat, delay):
    for _ in range(repeat):
        subprocess.run(["xdotool", "type", message])
        subprocess.run(["xdotool", "key", "Return"])
        time.sleep(delay)

def setup():
    # Add a 2-second delay before starting


    start_time = time.time()

    message = input("What message would you like to send?: ")
    repeat = int(input("How many times would you like to send it?: "))
    delay = float(input("How fast would you like the message (in seconds)?: "))
    print("Waiting for 2 seconds before starting...")
    time.sleep(2)
    send_message(message, repeat, delay)

    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

    # Count the number of words and letters in the message
    num_words = len(message.split())
    num_letters = sum(c.isalpha() for c in message)
    total_words_sent = repeat * num_words
    total_letters_sent = repeat * num_letters
    print(f"Total words sent: {total_words_sent}")
    print(f"Total letters sent: {total_letters_sent}")

setup()