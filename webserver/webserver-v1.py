from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Function to save form data to a CSV file
def save_to_csv(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Function to read data from CSV file
def read_from_csv():
    data = []
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    ip_address = request.form['ip-addres']
    password = request.form['passwrod']
    data = [ip_address, password]
    save_to_csv(data)
    return render_template('index.html', message="Data saved successfully!")

# Route to display data from CSV
@app.route('/data')
def display_data():
    data = read_from_csv()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
