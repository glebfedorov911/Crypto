FROM python:3.13-slim

EXPOSE 8015

WORKDIR /app

RUN apt-get update

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]