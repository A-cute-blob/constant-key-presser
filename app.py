import keyboard
import threading
import time

stop = threading.Event()
active = threading.Event()
user_input = threading.Event()

def keypress():
    while not stop.is_set():
        if active.is_set():
            print("Inactivity timer started.")
            time.sleep(10)
            active.clear()

            if stop.is_set():
                break

            print("Typing 'r' every second.")
            while not stop.is_set() and not active.is_set():
                user_input.clear()  
                keyboard.press_and_release('r')
                time.sleep(0.5)
        else:
            time.sleep(0.5)

def detect_input():
    while not stop.is_set():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'r' and not user_input.is_set():
                continue  
            active.set()
            user_input.set() 
            print("User input detected. Resetting inactivity timer.")
            time.sleep(1)

def main():
    st = threading.Thread(target=keypress)
    st.start()
    try:
        detect_input()
    except KeyboardInterrupt:
        stop.set()

main()
