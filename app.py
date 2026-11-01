# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
from queue import Queue, PriorityQueue

app = Flask(__name__)

# Sample data for doctors with specialization, room number, and availability
doctors = [
    {'name': 'Dr. John Doe', 'specialization': 'Physician', 'room_number': '101', 'availability': 'Available'},
    {'name': 'Dr. Jane Smith', 'specialization': 'Oncologist', 'room_number': '102', 'availability': 'Unavailable'},
    {'name': 'Dr. Emily White', 'specialization': 'Gynecologist', 'room_number': '103', 'availability': 'Available'},
    {'name': 'Dr. Michael Brown', 'specialization': 'Pediatrician', 'room_number': '104', 'availability': 'Available'},
    {'name': 'Dr. Sarah Green', 'specialization': 'Gastroenterologist', 'room_number': '105', 'availability': 'Unavailable'},
    {'name': 'Dr. Richard Black', 'specialization': 'Physician', 'room_number': '106', 'availability': 'Available'},
    {'name': 'Dr. Linda Blue', 'specialization': 'Cardiologist', 'room_number': '107', 'availability': 'Available'},
    {'name': 'Dr. Laura Gold', 'specialization': 'Neurologist', 'room_number': '108', 'availability': 'Unavailable'},
    {'name': 'Dr. Kevin White', 'specialization': 'Orthopedic Surgeon', 'room_number': '109', 'availability': 'Available'},
    {'name': 'Dr. Anna Gray', 'specialization': 'Psychiatrist', 'room_number': '110', 'availability': 'Unavailable'},
    {'name': 'Dr. Daniel Lee', 'specialization': 'Dermatologist', 'room_number': '111', 'availability': 'Available'},
    {'name': 'Dr. Emma Brown', 'specialization': 'Ophthalmologist', 'room_number': '112', 'availability': 'Available'}
]

# Initialize Queues
normal_queue = Queue()
emergency_queue = PriorityQueue()

# File to store patient data
CSV_FILE = 'patients.csv'

# Helper to get today's date
def get_today_date():
    return datetime.now().strftime("%d-%m-%Y")

# Load patients from CSV
patients = []
def load_patients():
    try:
        with open(CSV_FILE, newline='') as f:
            reader = csv.DictReader(f)
            patients.clear()
            for row in reader:
                patients.append(row)
    except FileNotFoundError:
        pass

# Save patients to CSV
def save_patients():
    with open(CSV_FILE, 'w', newline='') as f:
        fieldnames = ['name', 'gender', 'age', 'issue', 'room', 'doctor', 'status', 'type', 'fee', 'advance_paid', 'total_paid']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)

@app.route('/')
def index():
    load_patients()
    return render_template('index.html', doctors=doctors, patients=patients, date=get_today_date())

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    issue = request.form['issue']
    room = request.form.get('room', '')
    doctor = request.form['doctor']
    status = request.form['status']
    patient_type = request.form['type']
    fee = request.form['fee']
    advance_paid = 'advance_paid' in request.form
    total_paid = 'total_paid' in request.form

    patient = {
        'name': name,
        'gender': gender,
        'age': age,
        'issue': issue,
        'room': room,
        'doctor': doctor,
        'status': status,
        'type': patient_type,
        'fee': fee,
        'advance_paid': advance_paid,
        'total_paid': total_paid
    }

    # Add to appropriate queue
    if patient_type.lower() == 'emergency':
        emergency_queue.put((1, patient))
    else:
        normal_queue.put(patient)

    patients.append(patient)
    save_patients()
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_patient(index):
    if 0 <= index < len(patients):
        patients.pop(index)
        save_patients()
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('query', '')
    filtered = [p for p in patients if query.lower() in p['name'].lower()]
    return render_template('search_results.html', patients=filtered)

if __name__ == '__main__':
    app.run(debug=True)
