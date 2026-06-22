# Hospital Management System 🏥

A web-based Hospital Management System built using **Python Flask** and **Data Structures (Queue & Priority Queue)**.

> First Year DSA Course Project | B.Tech CSE

---

## 📌 About

This system manages hospital patients by distinguishing between **normal** and **emergency** cases, assigning doctors and rooms, and tracking treatment status — all through a clean web interface.

---

## ✨ Features

- Add patients with details: name, age, gender, health issue, fee status
- Separate queues for **Normal** and **Emergency** patients
- Assign doctors and room numbers to patients
- Track treatment status: Waiting → In Progress → Discharged
- Search patients by name
- Delete individual patients
- Export patient data to CSV
- Display available doctors with specialization and room numbers

---

## 🧠 Data Structures Used

| Structure | Usage |
|---|---|
| **Queue (FIFO)** | Normal patient management |
| **Priority Queue (Heap)** | Emergency patient management |

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Storage:** In-memory lists + optional CSV export

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/ashritha13046/Hospital_Flask_Project.git
cd Hospital_Flask_Project
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the app:**
```bash
python app.py
```

**4. Open in browser:**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
Hospital_Flask_Project/
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── templates/
│   └── index.html          # Frontend HTML
└── docs/
    ├── Hospital_management_system_ppt.pptx   # Presentation
    └── Hospital_Management_System.docx        # Project Report
```

---

## 👩‍💻 Developed By

**Gujjula Ashritha Reddy** | 2401MC35 | B.Tech MNC
