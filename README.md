# Hospital Management System

A simple web app built with **Python and Flask** to manage hospital patients using queue concepts from Data Structures.

## Features

- Register patients as **Normal** or **Emergency**
- Normal patients go into a FIFO queue; emergency patients go into a separate priority queue
- Assign a doctor and room, and track status (Waiting, In Treatment, Discharged)
- Doctor list with specialization, room number and availability
- Track fee, advance payment and total payment
- Search patients by name
- Delete patient records
- Patient data is saved in `patients.csv`

## Tech Stack

- Python 3, Flask
- HTML, CSS (Jinja2 templates)
- CSV file for storage
- Python `queue.Queue` and `queue.PriorityQueue`

## Project Structure

```
app.py                  Flask routes and queue logic
templates/
    index.html          Main page (doctors, add form, patient list)
    search_results.html Search results page
patients.csv            Saved patient data
requirements.txt        Dependencies
```

## How to Run

1. Install Python 3.8 or newer
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app from this folder:
   ```
   python app.py
   ```
4. Open **http://127.0.0.1:5000** in your browser

## Limitations

- Data is stored in a CSV file, not a database
- No login or user roles
- Patients are deleted by list position, not by a unique ID
- The queues are kept in memory and reset when the server restarts

## Future Improvements

- Use a database (SQLite/MySQL) with unique patient IDs
- Add login with roles (admin, doctor, receptionist)
- Use `heapq` with severity levels for a true priority queue
- Edit/update patient details
- Appointment booking and billing

## Author

Gujjula Ashritha Reddy 
