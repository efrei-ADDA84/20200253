FROM python:3.11-alpine

WORKDIR /app

COPY wrapper.py .

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHER_API_KEY="dd873b7df67e31543347c06989e163cc"

CMD ["python", "wrapper.py"]
