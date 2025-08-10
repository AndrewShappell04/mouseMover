import pyautogui
import time

# Wait 3 seconds to close command prompt
time.sleep(3)

# Get the center of the screen
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

# Move the mouse to the center of the screen
pyautogui.moveTo(center_x, center_y)

# Wait another 2 seconds
time.sleep(2)

run_for = 0

# Run script for  hour
while run_for < 12:
    # Moves the mouse right 100 pixels and down 50 pixels
    pyautogui.moveRel(xOffset=100, yOffset=50, duration=.75)
    time.sleep(299)
    run_for += 1


