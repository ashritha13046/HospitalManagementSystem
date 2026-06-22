from flask import Flask, render_template, request, jsonify, redirect
import heapq

app = Flask(__name__)

normal_queue = []
emergency_queue = []

doctors = ["Dr. A", "Dr. B", "Dr. C"]
available_doctors = doctors.copy()

available_rooms = ["E-101", "E-102", "E-103"]
used_rooms = []

@app.route('/')
def index():
    return render_template('index.html', normal_queue=normal_queue,
                           emergency_queue=emergency_queue,
                           doctors=available_doctors)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    issue = request.form['issue']
    category = request.form['category']

    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "issue": issue,
        "category": category,
        "status": "Waiting"
    }

    if category == "emergency":
        heapq.heappush(emergency_queue, (0, patient))
    else:
        normal_queue.append(patient)

    return redirect('/')

@app.route('/assign_doctor', methods=['POST'])
def assign_doctor():
    if emergency_queue and available_doctors and available_rooms:
        _, patient = heapq.heappop(emergency_queue)
        doctor = available_doctors.pop(0)
        room = available_rooms.pop(0)

        patient['doctor'] = doctor
        patient['room'] = room
        patient['status'] = "In Progress"

        normal_queue.append(patient)
        used_rooms.append(room)

        return jsonify({"status": "success", "patient": patient})
    else:
        return jsonify({"status": "error", "message": "No doctor or room available"})

@app.route('/mark_treated', methods=['POST'])
def mark_treated():
    name = request.form['name']
    for patient in normal_queue:
        if patient['name'] == name:
            patient['status'] = "Treated"
            if 'room' in patient:
                available_rooms.append(patient['room'])
                used_rooms.remove(patient['room'])
            if 'doctor' in patient:
                available_doctors.append(patient['doctor'])
            break
    return redirect('/')

@app.route('/delete_patient', methods=['POST'])
def delete_patient():
    name = request.form['name']
    found = False

    for i, (_, patient) in enumerate(emergency_queue):
        if patient['name'] == name:
            del emergency_queue[i]
            found = True
            break

    if not found:
        for i, patient in enumerate(normal_queue):
            if patient['name'] == name:
                if 'room' in patient:
                    available_rooms.append(patient['room'])
                    used_rooms.remove(patient['room'])
                if 'doctor' in patient:
                    available_doctors.append(patient['doctor'])
                del normal_queue[i]
                found = True
                break

    if found:
        return jsonify({"status": "success", "message": f"{name} deleted"})
    else:
        return jsonify({"status": "error", "message": f"{name} not found"})

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [p for p in normal_queue + [x[1] for x in emergency_queue] if query in p['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)