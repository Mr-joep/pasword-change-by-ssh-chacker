import os
import re
import time
import csv

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

def extract_ips(text):
    return re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

def remove_ips_from_csv(ip_list, csv_file_path):
    if os.path.exists(csv_file_path):
        try:
            with open(csv_file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)
            
            with open(csv_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for row in rows:
                    if row[0] not in ip_list:
                        writer.writerow(row)
            
            print("IP addresses removed from ip.csv")
        except Exception as e:
            print("Error while removing IP addresses from ip.csv:", e)
    else:
        print("ip.csv file not found. No IP addresses removed.")

def main():
    folder_path = r'C:\ip-shit\ssh_failure'  # Modify the folder path accordingly
    csv_file_path = r'C:\ip-shit\ip.csv'  # Modify the CSV file path accordingly

    while True:
        file = get_second_last_file(folder_path)
        if file:
            file_path = os.path.join(folder_path, file)
            print("Second-last file found:", file)
            file_content = read_file(file_path)
            print("File contents:")
            print(file_content)
            ip_list = extract_ips(file_content)
            print("IP addresses extracted:", ip_list)
            remove_ips_from_csv(ip_list, csv_file_path)
        else:
            print("No files found in the folder.")
        time.sleep(2)

if __name__ == "__main__":
    main()
