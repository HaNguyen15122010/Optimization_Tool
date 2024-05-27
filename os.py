import os
import shutil
import subprocess
import getpass
from telnetlib import EL  
import psutil

en = input("Enter to start .... ")
if en == "":
    
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
            "C:\\Windows\\Temp",
            f"C:\\Users\\{username}\\AppData\\Local\\Temp",
            f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files",
            "C:\\Windows\\SoftwareDistribution\\Download",
            "C:\\Windows\\Prefetch",
            "C:\\Windows\\Logs",
            "C:\\Windows\\Installer",
            "C:\\Windows\\System32\\LogFiles",
            "C:\\Windows\\WinSxS\\Temp",
            "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\Temporary ASP.NET Files",
            f"C:\\Users\\{username}\\Downloads" 
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

    def clean_memory():
        """
        This function reduces memory usage by terminating processes consuming excessive memory.
        """
        for proc in psutil.process_iter():
            try:
                process = psutil.Process(proc.pid)
                process_memory = process.memory_info().rss / (1024 * 1024)  # Convert to MB
           
                if process_memory > 100:
                    process.terminate()
                    print(f"Terminated process {process.name()} (PID: {process.pid}) to reduce memory usage.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    if __name__ == "__main__":
        main()
        clean_memory()

    while True: 
    
        ex = input("Enter to exit .... ")
        if ex == "":
            break
else:
    print("Program not run !")
