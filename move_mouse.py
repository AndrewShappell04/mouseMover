import pyautogui
import time

# Wait 3 seconds to close command prompt
time.sleep(3)

run_for = 0

# Run script for  hour
while run_for < 12:
    # Moves the mouse right 100 pixels and down 50 pixels
    pyautogui.moveRel(xOffset=100, yOffset=50, duration=.75)
    time.sleep(299)
    run_for += 1


