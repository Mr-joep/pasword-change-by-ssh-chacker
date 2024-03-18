import csv
import paramiko
from paramiko.ssh_exception import AuthenticationException
from datetime import datetime
import time
import os

def check_ssh(host, password, port=22, username="root"):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port, username=username, password=password, timeout=5)
        ssh.close()
        return True
    except AuthenticationException:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    while True:
        input_file = "ip.csv"
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        # Create a directory for success files
        success_dir = "ssh_success"
        if not os.path.exists(success_dir):
            os.makedirs(success_dir)

        success_file = os.path.join(success_dir, f"ssh_success_{timestamp}.csv")
        
        failure_dir = "ssh_failure"
        if not os.path.exists(failure_dir):
            os.makedirs(failure_dir)

        failure_file = os.path.join(failure_dir, f"ssh_failure_{timestamp}.csv")

        with open(input_file, newline='') as csvfile, \
                open(success_file, "w", newline='') as successcsv, \
                open(failure_file, "w", newline='') as failurecsv:

            reader = csv.DictReader(csvfile)

            success_fieldnames = reader.fieldnames + ['SSH Result']
            failure_fieldnames = reader.fieldnames + ['SSH Result']

            success_writer = csv.DictWriter(successcsv, fieldnames=success_fieldnames)
            success_writer.writeheader()

            failure_writer = csv.DictWriter(failurecsv, fieldnames=failure_fieldnames)
            failure_writer.writeheader()

            for row in reader:
                ip = row["ip-addresse"].strip()
                password = row["password"].strip()
                if ip and password:
                    if check_ssh(ip, password):
                        row['SSH Result'] = f"SSH is open on {ip}"
                        success_writer.writerow(row)
                    else:
                        row['SSH Result'] = f"SSH is not open on {ip}"
                        failure_writer.writerow(row)

        print(f"Results exported to {success_file} and {failure_file}")
        print("Waiting for an hour before starting over...")
        time.sleep(3)  # Sleep for one hour (3600 seconds)
