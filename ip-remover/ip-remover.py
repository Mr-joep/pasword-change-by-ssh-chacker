import os
import time

def get_second_last_file(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]  # Only files, not directories
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    if len(files) >= 2:
        return files[-2]
    else:
        return None

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    folder_path = 'C:\ip-shit\ssh_failure'

    while True:
        file = get_second_last_file(folder_path)
        if file:
            file_path = os.path.join(folder_path, file)
            print("Second-last file found:", file)
            print("File contents:")
            print(read_file(file_path))
        else:
            print("No files found in the folder.")
        time.sleep(2)

if __name__ == "__main__":
    main()
