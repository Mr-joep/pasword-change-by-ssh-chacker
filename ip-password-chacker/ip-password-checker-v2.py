import csv
import paramiko
from paramiko.ssh_exception import AuthenticationException

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
    input_file = "ip.csv"
    output_file = "ssh_results.csv"
    
    with open(input_file, newline='') as csvfile, open(output_file, "w", newline='') as outputcsv:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['SSH Result']
        writer = csv.DictWriter(outputcsv, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            ip = row["ip-addresse"].strip()
            password = row["password"].strip()
            if ip and password:
                if check_ssh(ip, password):
                    row['SSH Result'] = f"SSH is open on {ip}"
                else:
                    row['SSH Result'] = f"SSH is not open on {ip}"
                print(row['SSH Result'])
                writer.writerow(row)

    print(f"Results exported to {output_file}")
