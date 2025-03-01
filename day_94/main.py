import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab

def press_space():
    pyautogui.press("space")

def detect_obstacle():
    # Define the region of interest (ROI) where obstacles appear
    x, y, width, height = 500, 380, 100, 50  # Adjust for your screen resolution
    
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    image = np.array(screenshot)
    
    # Convert to grayscale for easier processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold to detect obstacles
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Count non-zero pixels (indicating an obstacle)
    if np.sum(thresh) > 1000:
        return True
    return False

def play_trex():
    print("Starting T-Rex bot in 3 seconds...")
    time.sleep(3)
    press_space()  # Start the game
    
    while True:
        if detect_obstacle():
            press_space()
        time.sleep(0.05)  # Adjust speed for better accuracy

if __name__ == "__main__":
    play_trex()
