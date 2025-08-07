import pyautogui

print(dir(pyautogui))


screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

print(f"Center of screen: ({center_x}, {center_y})")


print(help(pyautogui.size))

print(pyautogui.size())