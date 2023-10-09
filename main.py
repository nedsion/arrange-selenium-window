from selenium import webdriver
import tkinter as tk

# Get the screen width and height using tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Number of rows and columns
num_rows = 3
num_columns = 3

# Calculate window width and height for each tab
window_width = screen_width // num_columns
window_height = screen_height // num_rows

# List to store WebDriver instances
drivers = []

# Create and arrange Selenium tabs row by row
for row in range(num_rows):
    for column in range(num_columns):
        # Calculate the position of the tab
        x_position = column * window_width
        y_position = row * window_height
        
        # Create a new Chrome browser instance
        driver = webdriver.Chrome()
        
        # Set the position and size of the browser window
        driver.set_window_position(x_position, y_position)
        driver.set_window_size(window_width, window_height)
        
        # Append the WebDriver instance to the list
        drivers.append(driver)

# Example: Navigate each tab to a different website
for i, driver in enumerate(drivers):
    driver.get(f"https://www.example{i + 1}.com")

# Do your automation tasks here for each tab

# Close all the browser windows when you're done
input("Press Enter to close all browser windows...")
for driver in drivers:
    driver.quit()
