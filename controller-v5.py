import subprocess
import platform

def start_script(script_path):
    if platform.system() == "Windows":
        return subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        return subprocess.Popen(["python3", script_path])

def start_other_scripts(script1_path, script2_path):
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
        print("0. Exit")

        choice = input("Enter the number of the action to perform: ")

        if choice == "1":
            if process1.poll() is None:
                stop_script(process1)
                print("Script 1 has been stopped.")
            else:
                process1 = start_script(script1_path)
                print("Script 1 has been started.")
        elif choice == "2":
            if process2.poll() is None:
                stop_script(process2)
                print("Script 2 has been stopped.")
            else:
                process2 = start_script(script2_path)
                print("Script 2 has been started.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    script1_path = "C:\ip-shit\ip-password-checker-v6.py"  # Change this to the path of your first script
    script2_path = "C:\ip-shit\ip-remover-v2.py"  # Change this to the path of your second script
    process1, process2 = start_other_scripts(script1_path, script2_path)
    main_menu(process1, process2)
