
# Use a minimal base image with Python 3.9 installed
FROM python:3.9

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the entire project structure into the container
COPY . /app

# Install Python dependencies from the deployment-specific requirements.txt
RUN pip3 install -r deployment/requirements.txt

# Create a non-root user for security best practices
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user     PATH=/home/user/.local/bin:$PATH

# Streamlit app needs to be run from its directory or referred to by its full path
# Assuming app.py is at /app/deployment/app.py
CMD ["streamlit", "run", "deployment/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
