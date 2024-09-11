# Auto Keyboard Presser with Inactivity Timer

This script automatically detects user input and presses a key (default: 'r') every 0.5 seconds after 10 seconds of inactivity. The key pressed upon inactivity can be easily customized.

## Features
- **Inactivity Timer**: A 10-second countdown begins after no user input is detected.
- **Auto Typing**: Once the countdown finishes, the script will simulate pressing the 'r' key every 0.5 seconds.
- **Real-Time Input Detection**: Any detected keypress will reset the inactivity timer and prevent the automated typing.

## How It Works
- **`keypress()`**: This function runs in a separate thread and monitors for inactivity. If no user input is detected for 10 seconds, it starts typing 'r' every 0.5 seconds.
- **`detect_input()`**: This function constantly detects keyboard input and resets the inactivity timer when the user presses a key. It ensures that 'r' typed by the script is ignored during detection.

## Installation
1. Install the required `keyboard` library:
   ```bash
   pip install keyboard
