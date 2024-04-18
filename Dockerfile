FROM python:3.11-alpine

WORKDIR /app

COPY tp1devopps.py .

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHER_API_KEY=""
ENV FLASK_APP=weather.py

CMD ["python", "wrapper.py"]
