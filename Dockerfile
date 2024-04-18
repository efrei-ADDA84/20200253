FROM python:3.11-alpine

WORKDIR /app

COPY wrapper.py .

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHER_API_KEY=""
ENV FLASK_APP=wrapper.py

CMD ["python", "wrapper.py"]
