import os
import shutil
import subprocess
import getpass  

print("Enter to run ... ")
def clean_directory(folder):
    """
    This function recursively walks through all files and directories in `folder`,
    and deletes all files and directories within it.
    """
    for root, subdirectories, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.access(file_path, os.W_OK):
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)
                else:
                    print(f"Permission denied: {file_path} - Skipping...")
            except Exception as e:
                print(f"Error while deleting file: {file_path} - {e}")

    for root, subdirectories, files in os.walk(folder, topdown=False):
        for subdirectory in subdirectories:
            try:
                directory_path = os.path.join(root, subdirectory)
                print(f"Deleting directory: {directory_path}")
                shutil.rmtree(directory_path)
            except Exception as e:
                print(f"Error while deleting directory: {directory_path} - {e}")

def defragment_drive(drive):
    """
    This function defragments the specified drive using the Windows defrag utility.
    """
    try:
        print(f"Defragmenting drive: {drive}")
        subprocess.run(["defrag", drive, "/C"])  
        print(f"Drive {drive} defragmentation completed.")
    except Exception as e:
        print(f"Error while defragmenting drive {drive}: {e}")

def main():
    username = getpass.getuser()  
    folders_to_clean = [
        "C:\\Windows\\Temp"
        f"C:\\Users\\{username}\\AppData\\Local\\Temp"
        f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files"
        "C:\\Windows\\SoftwareDistribution\\Download"
        "C:\\Windows\\Prefetch"
        "C:\\Windows\\Logs"
        "C:\\Windows\\Installer"
        "C:\\Windows\\System32\\LogFiles"
        "C:\\Windows\\WinSxS\\Temp"
        "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\Temporary ASP.NET Files"
    ]

    drives_to_defrag = [
        "C:",
        "D:",
        
    ]

    for folder_to_clean in folders_to_clean:
        if not os.path.isdir(folder_to_clean):
            print(f"Invalid or non-existent directory path: {folder_to_clean}")
        else:
            print(f"Cleaning directory: {folder_to_clean}")
            clean_directory(folder_to_clean)
    
    for drive_to_defrag in drives_to_defrag:
        defragment_drive(drive_to_defrag)
    
    print("Cleanup and defragmentation completed.")

if __name__ == "__main__":
    main()

while True: 
    
    ex = input("Enter x to exit .... ")
    if ex == "x":
        break
