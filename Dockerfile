# Dockerfile

FROM python:3.9-slim
WORKDIR /app

# Copy requirements from the root and install them first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code from the 'src' directory
COPY src/ .

ENV GREETING="Hi there"
EXPOSE 5000
CMD ["python", "app.py"]