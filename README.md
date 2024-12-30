# Face Attendance System App

Welcome to the **Face Attendance System App**! This Python-based application leverages **InsightFace** for facial recognition and **Streamlit** for its user-friendly interface. Developed by **Harsh Vaidya**, this project provides a seamless way to manage attendance using advanced facial recognition technology.

We invite open-source contributors to enhance this project further! 🚀

## About the Project

The **Face Attendance System App** is designed to simplify attendance management by leveraging facial recognition. This project is perfect for use in classrooms, offices, or any setting where attendance tracking is required.

## Features

- **Real-Time Facial Recognition:** Utilizes the powerful InsightFace library for accurate and efficient facial recognition
- **Streamlit Interface:** A simple, interactive, and user-friendly web-based interface
- **Redis Integration:** Enables fast data storage and retrieval for real-time performance
- **Open Source:** Contributions are welcome from developers worldwide!

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/harsh432004/attendance-system-app
   ```

2. **Navigate to Project Directory**
   ```sh
   cd attendance-system-app
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```sh
   streamlit run app.py
   ```

5. **Access the App**  
   Open your browser and visit http://localhost:8501

## Project Setup for Contributors

### Setting Up the Development Environment

1. **Set Up Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Required Libraries**
   ```sh
   pip install -r requirements.txt
   pip install insightface
   ```

3. **Download Required Models**
   - Download the buffalo_l and buffalo_sc models from the official InsightFace repository
   - Place the downloaded models in the appropriate directory within the project

4. **Set Up Redis**
   - Install and set up a Redis instance
   - You can use Redis Cloud or install Redis locally on your machine

5. **Run for Development**
   ```sh
   streamlit run app.py
   ```
## Docker Setup

1. **Build the Docker image:**
   ```bash
   docker build -t attendance-system-app .
## Contributing

1. **Fork the Repository**
   - Click the "Fork" button at the top-right corner

2. **Create a Branch**
   ```sh
   git checkout -b feature-name
   ```

3. **Make Changes**
   - Add your changes and test thoroughly

4. **Commit Changes**
   ```sh
   git commit -m "Description of changes"
   ```

5. **Push Changes**
   ```sh
   git push origin feature-name
   ```

6. **Create Pull Request**
   - Submit a pull request with clear description of changes

### Contribution Guidelines
- Ensure code adheres to project's coding standards
- Test changes locally before submitting
- Include comments and documentation for new features

## Fun-Fact

This project can be used in your college project and also used in hackathons 😀

## Deploymet Guide
- For more information on how to deploy the Attendance System, check out the documentation at [Attendance System Deployment Docs](https://attendance-system-app-deploymentdocs.vercel.app/).


## Contributors

- Harsh Vaidya - Lead Developer
- Want to see your name here? Contribute to the project!

## Support

For inquiries, issues, or support:

**Harsh Vaidya**  
📧 Email: harshvaidya432004@gmail.com

You can also create an issue in the repository for bugs, feature requests, or questions.
