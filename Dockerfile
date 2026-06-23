FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY index.html .
COPY app.js .
COPY server.py .

EXPOSE 5000

ENV FLASK_APP=server.py
ENV FLASK_ENV=production

CMD ["python", "server.py"]
