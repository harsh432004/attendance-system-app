# Use a base Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Copy the .env file
COPY .env /app/.env

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    numpy pandas opencv-python-headless insightface redis scikit-learn streamlit

# Create a non-root user and switch to it
RUN useradd -ms /bin/bash appuser
USER appuser

# Expose the default Streamlit port
EXPOSE 8501

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
