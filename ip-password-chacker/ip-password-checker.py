import csv
import socket

def check_ssh(host, port=22):
    try:
        # Attempt to establish a TCP connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Timeout for connection attempt
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
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
            if ip:
                if check_ssh(ip):
                    row['SSH Result'] = f"SSH is open on {ip}"
                else:
                    row['SSH Result'] = f"SSH is not open on {ip}"
                print(row['SSH Result'])
                writer.writerow(row)

    print(f"Results exported to {output_file}")
