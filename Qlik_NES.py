import pygame
import pyautogui
import keyboard
import time

# Initialize Pygame and the controller
pygame.init()
pygame.joystick.init()

# Assuming only one joystick connected
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Sensitivity of mouse movements (adjust as needed)
mouse_sensitivity = 1
input_multiplier=50
scroll_sensitivity = 10  # Adjust the scroll speed

def map_controller_to_mouse():
    while True:
        pygame.event.pump()
        
        # D-pad movements (axes 0, 1 for x and y respectively)
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        # Move mouse based on D-pad axis
        if abs(x_axis) > 0.1:  # Small threshold to avoid drifting
            pyautogui.moveRel(x_axis * mouse_sensitivity*input_multiplier, 0)
        
        if abs(y_axis) > 0.1:
            pyautogui.moveRel(0, y_axis * mouse_sensitivity*input_multiplier)

        # Button mappings: adjust button indices based on your controller's button layout
        # Example: NES controller buttons (you can find these via pygame's Joystick methods)
        
        


        # Left-click
        if joystick.get_button(0):  # Replace with correct button index
            pyautogui.click(button='left')
        
        # Right-click
        if joystick.get_button(1):  # Replace with correct button index
            pyautogui.click(button='right')

        # Trigger "Win + Tab" to open Task View (bind to input 10)
        # if joystick.get_button(8):  # Button 10 index for your controller
        #     keyboard.press_and_release('win+tab')

        if joystick.get_button(8):
            # Scroll up/down with the Y-axis (up is negative, down is positive)
            if abs(y_axis) > 0.1:
                pyautogui.scroll(-y_axis * scroll_sensitivity)

            # Optionally, horizontal scrolling with X-axis (remove if not needed)
            if abs(x_axis) > 0.1:
                pyautogui.hscroll(x_axis * scroll_sensitivity)


        # Exit loop with a certain button press (optional)
        if joystick.get_button(9):  # Replace with the correct index (maybe "Start" button)
            print("Exiting")
            break

        time.sleep(0.001)  # Small delay to prevent excessive CPU usage

# Run the controller-to-mouse mapping
try:
    map_controller_to_mouse()
finally:
    # Quit pygame properly
    pygame.joystick.quit()
    pygame.quit()
