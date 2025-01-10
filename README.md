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
git clone https://github.com/harsh432004/attendance-system-app
### 2. Navigate to The project directory
cd attendance-system-app
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the Application
streamlit run app.py
### 5. Access the App
Open your web browser and visit: http://localhost:8501
For a live demo, visit the deployed version at: 13.60.199.34

# 🔧 Project Setup for Contributors

To contribute effectively, follow these detailed setup instructions:
## 🚀 How to Run the Project
Follow the steps below to set up and run the project locally:

### 1. Clone the Repository
Clone the repository to your local machine using the following command:
git clone https://github.com/your-username/attendance-system-app
### 2. Navigate to the Project Directory
Move to the project folder:
cd attendance-system-app
### 3. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
### 4. Install Required Libraries
pip install -r requirements.txt
pip install insightface
### 5. Download Required Models
Download the buffalo_l and buffalo_sc models from the official InsightFace repository.
Place the downloaded models in the appropriate directory within the project.
### 6. Set up Redis
Install and configure a Redis instance.
You can use either Redis Cloud or install Redis locally on your machine.
### 7. Run for Development
streamlit run app.py


## 🤝 Contributing
We welcome contributions to enhance this project! Here's how you can get involved:

### Steps to Contribute

#### 1. Fork the Repository
- Click the "Fork" button at the top-right corner of the repository.

#### 2. Create a Branch
git checkout -b feature-name

### 3. Make Changes
Implement your changes and test thoroughly.
### 4. Commit Changes
git commit -m "Description of changes"
### 5. Push Changes
git push origin feature-name
### 6. Create a Pull Request
Submit a pull request with a clear description of your changes.

### Contribution Guidelines
- Ensure code adheres to the project's coding standards.
- Test changes locally before submitting.
- Provide comments and documentation for new features.

---
## 🚀 How to Deploy the Project

To deploy the project in a production environment, follow these steps:

### 1. Docker Setup

#### Build the Docker Image
Build the Docker image for the project with the following command:
docker build -t attendance-system-app .

#### Run the Docker Container
Run the container with the following command:
docker run -p 8501:8501 attendance-system-app
Access the application at http://localhost:8501.

---

# 📋 Code of Conduct

We are committed to creating a welcoming and inclusive environment for all contributors. By participating in this project, you agree to adhere to the following guidelines:

1. **Respectful Communication:** Be respectful and courteous to others. Harassment or discriminatory behavior will not be tolerated.
2. **Constructive Feedback:** Provide constructive feedback and be open to receiving it.
3. **Inclusive Environment:** Embrace diversity and encourage everyone to contribute, regardless of background or experience level.
4. **Collaboration:** Collaborate with others to solve problems, share knowledge, and improve the project.
5. **Stay Professional:** Keep discussions relevant to the project and refrain from inappropriate content.

---

## 📖 Fun Fact
This project is perfect for college projects and hackathons and demonstrates the practical application of advanced technologies like facial recognition.

---

## 👨‍💻 Contributors
- **Harsh Vaidya** - Lead Developer

Want to see your name here? Contribute to the project!

---

## 📞 Support
For inquiries, issues, or support:

- **Harsh Vaidya**  
- 📧 Email: harshvaidya432004@gmail.com  
- Alternatively, create an issue in the GitHub repository for bugs, feature requests, or questions.

---

## 🌐 Live Demo
Check out the live demo of the application at: `13.60.199.34`

---

## 🎉 Interactive Features
- **QR Code Attendance:** Generate and scan QR codes for instant attendance marking.
- **Customizable Alerts:** Set notifications for late arrivals or absentees.
- **Language Support:** Multi-language support for diverse user bases.
- **Graphical Insights:** View attendance trends and statistics with interactive charts.
- **API Integration:** Integrate with third-party systems for extended functionality.
- **Custom Reports:** Generate attendance summaries and detailed reports on demand.
- **AI-Powered Insights:** Use machine learning to predict attendance trends and identify anomalies.

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---


