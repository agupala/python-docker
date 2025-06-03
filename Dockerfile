FROM python:3.11-slim

COPY app.py /app/

WORKDIR /app

CMD ["python", "app.py"]