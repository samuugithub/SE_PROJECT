FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Agent code
COPY . .

# Run your notification script
CMD ["python", "agent.py"]
