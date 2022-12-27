import os
import glob
import tkinter as tk
# Set the path to the directory where the new folder should be created
directory = 'D:\Projects'
# Set the name of the new folder
folder_name = 'new project'
# Check for duplicate folder names in the directory
existing_folders = glob.glob(os.path.join(directory, folder_name + '*'))


if existing_folders:
    # Try to find the highest number appended to the folder name
    try:
        highest_number = max([int(folder.split('_')[-1]) for folder in existing_folders if folder.split('_')[-1].isdigit()])
    # If there are no numbers appended to the folder name, set the highest number to 0
    except ValueError:
        highest_number = 0
    # Increment the number and append it to the folder name
    folder_name += f'_{highest_number + 1}'

# Create the new folder
os.makedirs(os.path.join(directory, folder_name))
created_directory_path = os.path.join(directory, folder_name)

# Create the blank readme.txt file
with open(os.path.join(directory, folder_name, 'readme.txt'), 'w') as f:
    pass

# Create the blank main.js file
with open(os.path.join(directory, folder_name, 'main.js'), 'w') as f:
    pass

# Create the html file
html = """<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-color: black;
      color: white;
      text-align: center;
      font-family: Arial Black;
    }
  </style>
</head>
<body>
  <h1><b>Welcome to my web sight></b></h1>
<h2>
  <script></script>
  <footer>&copy; 2022 IsaTech Inc.</footer>
</body>
</html>"""

with open(os.path.join(directory, folder_name, 'index.html'), 'w') as f:
    f.write(html)


# Create the main window
window = tk.Tk()
window.title("Task Completed")

# Create a label to display a message
label = tk.Label(window, text="The task was completed successfully.")
label.pack()

# Create a function for the "Close" button
def close_window():
    window.destroy()

# Create a function for the "Open in Explorer" button v2
def open_in_explorer():
    # Use the directory path that was saved in the created_directory_path variable
    directory = created_directory_path
    # Open the folder in a new Windows Explorer window
    os.system(f'start explorer "{directory}"')

# Create a function for the "Open in VS Code" button
def open_in_vs_code():
    # Use the directory path that was saved in the created_directory_path variable
    directory = created_directory_path
    # Close the dialog box
    window.destroy()
    # Open the folder in a new Visual Studio Code window
    os.system(f'start code "{directory}"')


# Create the "Close" button
close_button = tk.Button(window, text="Close", command=close_window)
close_button.pack()

# Create the "Open in Explorer" button
explorer_button = tk.Button(window, text="Open in Explorer", command=open_in_explorer)
explorer_button.pack()

# Create the "Open in VS Code" button
vs_code_button = tk.Button(window, text="Open in VS Code", command=open_in_vs_code)
vs_code_button.pack()

# Run the main loop
window.mainloop()

