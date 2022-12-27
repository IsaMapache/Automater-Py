import os
import platform
import subprocess
import requests
import json
import ctypes
from tkinter import Tk, Label, Button, filedialog


# Check the current operating system
if not platform.system() == "Windows":
    print("This script only works on Windows.")
    exit()

# Function to get the current version of the NVIDIA GPU driver
def get_current_driver_version():
    # Get the current GPU driver version using the 'wmic' command
    output = subprocess.check_output(["wmic", "datafile", "where", "name='C:\\\\Windows\\\\System32\\\\DriverStore\\\\FileRepository\\\\nv_disp.inf_amd64_none_8daa59a6939e4f87\\\\nvlddmkm.sys'" , "get", "Version"]).decode().strip()

    # The output of the command has multiple lines, so we need to get the second line (which contains the version number)
    lines = output.split("\n")
    if len(lines) < 2:
        return None
    return lines[1].strip()

# Function to get the latest version of the NVIDIA GPU driver from the NVIDIA website
def get_latest_driver_version():
    # Make a GET request to the NVIDIA API to get the latest driver version
    r = requests.get("https://api.nvidia.com/v1/drivers/current")

    # Check the status code of the response
    if r.status_code != 200:
        return None

    # Parse the JSON response
    data = r.json()

    # Get the version number from the JSON data
    return data["latest_driver_version"]

# Function to download the latest NVIDIA GPU driver from the NVIDIA website
def download_driver(filename):
    # Make a GET request to the NVIDIA download URL
    r = requests.get("https://www.nvidia.com/download/driverResults.aspx/160536/en-us")

    # Check the status code of the response
    if r.status_code != 200:
        return False

    # Write the file to the specified filename
    with open(filename, "wb") as f:
        f.write(r.content)
    return True

# Function to install the downloaded NVIDIA GPU driver
def install_driver(filename):
    # Run the driver installation file using the 'start' command
    subprocess.call(["start", filename, "/S"])

# Function to create a pop-up window with the update options
def create_popup():
    # Create a Tkinter root window
    root = Tk()
    root.title("NVIDIA GPU Driver Update")

    # Create a label to display the message
    label = Label(root, text="A newer version of the NVIDIA GPU driver is available. Do you want to download and install it now?")
    label.pack()

    # Create a "Download and Install" button
    def download_and_install():
        # Download the driver
        if not download_driver("nvidia_driver.exe"):
            print("Failed to download the driver.")
            return

        # Install the driver
        install_driver("nvidia_driver.exe")

        # Close the pop-up window
        root.destroy()

    download_install_button = Button(root, text="Download and Install", command=download_and_install)
    download_install_button.pack()

    # Create a "Download Only" button
    def download_only():
        # Download the driver
        if not download_driver("nvidia_driver.exe"):
            print("Failed to download the driver.")

        # Close the pop-up window
        root.destroy()

    download_only_button = Button(root, text="Download Only", command=download_only)
    download_only_button.pack()

    # Create a "Cancel" button
    def cancel():
        # Close the pop-up window
        root.destroy()

    cancel_button = Button(root, text="Cancel", command=cancel)
    cancel_button.pack()

    # Run the Tkinter event loop
    root.mainloop()


# Get the current and latest NVIDIA GPU driver versions
current_version = get_current_driver_version()
latest_version = get_latest_driver_version()

# Compare the versions and show the pop-up window if an update is available
if current_version is None:
    print("Failed to get the current NVIDIA GPU driver version.")
elif latest_version is None:
    print("Failed to get the latest NVIDIA GPU driver version.")
elif current_version < latest_version:
    create_popup()
else:
    print("The current NVIDIA GPU driver is up to date.")