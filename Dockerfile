# Python ki lightweight official image use kar rahe hain
FROM python:3.12-slim

# Container ke andar application ka working directory
WORKDIR /app

# Dependencies wali file container mein copy karo
COPY requirements.txt .

# Python dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Project ki baaki files container mein copy karo
COPY . .

# Flask application ka port expose karo
EXPOSE 5000

# Container start hone par Flask application run karo
CMD ["python", "app.py"]