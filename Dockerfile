# Base image
FROM python:3.9-slim

# Copy the current directory contents into the container
COPY . .

# Install the dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Set the environment variable for the MongoDB URI
ENV MONGO_URI="mongodb://localhost:27017/"

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
