FROM python:3.11-slim

# Install system dependencies for ReportLab fonts
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY templates/ ./templates/

# Create uploads directory
RUN mkdir -p uploads

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
