FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

COPY ../python-app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ../python-app/ .

EXPOSE 8000

CMD ["python", "app.py"]
