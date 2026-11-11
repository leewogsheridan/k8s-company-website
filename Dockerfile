from python:3.16-rc-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -m --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
