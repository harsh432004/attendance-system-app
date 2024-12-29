# Contributing to the Face Recognition System with Streamlit

Thank you for considering contributing to this project! We are excited to have you on board. This repository is a **Face Recognition System** built with **Streamlit**, **Python**, and **Redis DB**. To maintain a high-quality codebase, we ask that you follow these guidelines.

## Table of Contents

- [Contributing to the Face Recognition System with Streamlit](#contributing-to-the-face-recognition-system-with-streamlit)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [1. Fork the Repository](#1-fork-the-repository)
    - [2. Clone Your Fork](#2-clone-your-fork)
    - [3. Install Dependencies](#3-install-dependencies)
  - [How to Contribute](#how-to-contribute)
    - [Opening an Issue](#opening-an-issue)
    - [Pull Requests](#pull-requests)
  - [Code Style](#code-style)
    - [Python Formatting](#python-formatting)
    - [Linting](#linting)
  - [Running the Project Locally](#running-the-project-locally)
  - [Setting Up Pre-commit Hooks](#setting-up-pre-commit-hooks)
    - [Install Pre-commit](#install-pre-commit)
    - [Install the Hooks](#install-the-hooks)
    - [Running Pre-commit Hooks](#running-pre-commit-hooks)
  - [Opening an Issue](#opening-an-issue-1)
  - [Questions](#questions)
  - [Thank You!](#thank-you)

## Getting Started

To contribute, follow these steps to get a local copy of the project set up:

### 1. Fork the Repository

Click the **Fork** button in the top right corner of the repository page to create a copy of this repository under your GitHub account.

### 2. Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/your-username/face-recognition-system.git
```

### 3. Install Dependencies

Navigate to the project folder and install the required dependencies:

```bash
cd face-recognition-system
pip install -r requirements.txt
```

## How to Contribute

### Opening an Issue

If you find a bug, have a feature request, or need help, please feel free to open an issue. When opening an issue:

- Be descriptive and provide as much context as possible
- Use the provided issue templates if applicable

### Pull Requests

We welcome contributions in the form of pull requests! Here's how to submit one:

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Brief description of your changes"
```

3. Push your changes:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request:
   - Go to the original repository and open a pull request
   - Ensure your PR follows the project structure
   - Verify it doesn't break existing functionality
   - Include tests or clear explanations for new features

## Code Style

We use the following code style guidelines:

### Python Formatting
Use Black for automatic formatting:

```bash
# Check formatting
black --check .

# Format code
black .
```

### Linting
We use Flake8 to check code quality:

```bash
flake8 .
```

## Running the Project Locally

1. Start Redis Server:
```bash
redis-server
```

2. Run Streamlit App:
```bash
streamlit run app.py
```

3. Access the app at http://localhost:8501

## Setting Up Pre-commit Hooks

### Install Pre-commit
```bash
pip install pre-commit
```

### Install the Hooks
```bash
pre-commit install
```

### Running Pre-commit Hooks
```bash
pre-commit run --all-files
```

## Opening an Issue

When opening an issue:
- Be descriptive about the problem
- Include steps to reproduce the issue
- For feature requests, explain the feature in detail and why it would be beneficial
- ## 🚨 Reporting Issues

We use different issue templates to track various types of issues. When creating a new issue, please select the appropriate template from the list:

- 🐞 **Bug Report** – If you found a bug or error in the system.
- 🔖 **Documentation Update** – If you think the documentation needs improvements.
- ✨ **Feature Request** – If you have an idea for a new feature or enhancement.
- 👯‍♂️ **Style Change Request** – If you would like to suggest changes to the design or styling.
- ⚠️ **Security Vulnerability** – If you discovered a security issue, please follow our security policy.

Click on the "New issue" button above to get started, and please select the relevant template!


## Questions

If you have any questions, feel free to reach out through:
- The Issues section
- Discussions section in the repository

We are happy to assist you!

## Thank You!

We are excited to have you contribute to the project! By following these guidelines, you'll help ensure that the project stays clean, maintainable, and easy to use for everyone.

Happy coding! 😄
