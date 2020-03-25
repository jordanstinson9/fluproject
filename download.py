# ImmPort DataBrowser download script
import sys
import os
import pandas as pd

# Set base directory
BASE_DIR = os.getcwd()
print(BASE_DIR)

# Change directory Location to import the downloader
# Assumes there is a folder named immport-data-download-tool
immport_download_code = os.path.join(BASE_DIR,
                                    "immport-data-download-tool",
                                    "bin")
sys.path.insert(0,immport_download_code)
os.chdir(immport_download_code)
print(os.getcwd())

# Import the downloader script
import immport_download

# Return to base directory
os.chdir(BASE_DIR)
print(os.getcwd())

# Set configurations for downloading
user_name = "izumidk"
password = "20440Project!"
# Need to have output folders nested in directory
download_directory = "../output"
data_directory = "../data"

# Download files
# Download_file(user_name, password, path to study, download_directory)
immport_download.download_file(user_name, password,
                               "/SDY640", download_directory)
