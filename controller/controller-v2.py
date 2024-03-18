import subprocess
import platform
import time

def start_other_scripts():
    script1_path = "C:\ip-shit\ip-password-checker-v6.py"  # Change this to the path of your first script
    script2_path = "C:\ip-shit\ip-remover.py"  # Change this to the path of your second script

    if platform.system() == "Windows":
        process1 = subprocess.Popen(["python", script1_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        process2 = subprocess.Popen(["python", script2_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        process1 = subprocess.Popen(["python3", script1_path])
        process2 = subprocess.Popen(["python3", script2_path])

    return process1, process2

def stop_script(process):
    process.terminate()

def main_menu(process1, process2):
    while True:
        print("Running Scripts:")
        print("1. Script 1 -", "Running" if process1.poll() is None else "Stopped")
        print("2. Script 2 -", "Running" if process2.poll() is None else "Stopped")
        print("0. Exit")

        choice = input("Enter the number of the script to stop (or 0 to exit): ")

        if choice == "1":
            stop_script(process1)
            print("Script 1 has been stopped.")
        elif choice == "2":
            stop_script(process2)
            print("Script 2 has been stopped.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    process1, process2 = start_other_scripts()
    main_menu(process1, process2)
