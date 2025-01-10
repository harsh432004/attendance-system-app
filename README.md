# Face Attendance System App

Welcome to the **Face Attendance System App**! This Python-based application utilizes advanced facial recognition technology powered by **InsightFace** and features an intuitive, web-based interface developed with **Streamlit**. Created by **Harsh Vaidya**, this project aims to provide a seamless and efficient solution for managing attendance in various settings like classrooms, offices, and more.

---

## 🌟 Key Features

- **Real-Time Facial Recognition**: Leverages the robust InsightFace library for accurate and efficient recognition.
- **Interactive Streamlit Interface**: A user-friendly web-based interface for easy interaction.
- **Redis Integration**: Supports fast data storage and retrieval for real-time performance.
- **Attendance History Management**: Maintains a detailed log of attendance records with timestamps.
- **Customizable Models**: Easily replace or upgrade the facial recognition model as needed.
- **Multi-User Support**: Allows multiple users to access the system simultaneously without performance degradation.
- **Role-Based Access Control**: Implement different access levels (e.g., Admin, User) for enhanced security.
- **Cross-Platform Compatibility**: Accessible from any device with a web browser.
- **Email Notifications**: Automatically sends attendance reports to predefined email addresses.
- **Exportable Data**: Supports exporting attendance logs to CSV or Excel for further analysis.
- **Mobile-Friendly UI**: Optimized for both desktop and mobile devices.
- **Dark Mode**: Toggle between light and dark themes for better user experience.

---

## 📥 Getting Started

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/harsh432004/attendance-system-app

### 2. Navigate to the Project Directory
```bash
cd attendance-system-app
## 3. Install Dependencies
To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt

### 4. Run the Application
bash
Copy code
streamlit run app.py
### 5. Access the App
Open your web browser and visit: http://localhost:8501
For a live demo, visit the deployed version at: 13.60.199.34

# 🔧 Project Setup for Contributors

To contribute effectively, follow these detailed setup instructions:

## Setting Up the Development Environment

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
##Install Required Libraries
bash
Copy code
pip install -r requirements.txt
pip install insightface
