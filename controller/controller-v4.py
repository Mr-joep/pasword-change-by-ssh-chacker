import subprocess
import platform
import os

def start_script(script_path):
    if platform.system() == "Windows":
        return subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        return subprocess.Popen(["python3", script_path])

def start_other_scripts():
    script1_path = "path/to/your/script1.py"  # Change this to the path of your first script
    script2_path = "path/to/your/script2.py"  # Change this to the path of your second script

    process1 = start_script(script1_path)
    process2 = start_script(script2_path)

    return process1, process2

def stop_script(process):
    process.terminate()

def main_menu(process1, process2):
    while True:
        print("Running Scripts:")
        print("1. Script 1 -", "Running" if process1.poll() is None else "Stopped")
        print("2. Script 2 -", "Running" if process2.poll() is None else "Stopped")
        print("3. Start a script")
        print("0. Exit")

        choice = input("Enter the number of the action to perform: ")

        if choice == "1":
            if process1.poll() is None:
                stop_script(process1)
                print("Script 1 has been stopped.")
            else:
                process1 = start_script("path/to/your/script1.py")
                print("Script 1 has been started.")
        elif choice == "2":
            if process2.poll() is None:
                stop_script(process2)
                print("Script 2 has been stopped.")
            else:
                process2 = start_script("path/to/your/script2.py")
                print("Script 2 has been started.")
        elif choice == "3":
            script_path = input("Enter the path of the script to start: ")
            if os.path.exists(script_path):
                new_process = start_script(script_path)
                print("Script has been started.")
                # Assign the new process to appropriate variable based on user input
                if script_path.endswith("script1.py"):
                    process1 = new_process
                elif script_path.endswith("script2.py"):
                    process2 = new_process
            else:
                print("Invalid script path.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    process1, process2 = start_other_scripts()
    main_menu(process1, process2)
