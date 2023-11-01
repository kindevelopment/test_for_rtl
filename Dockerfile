FROM python:3.11-slim

RUN apt-get update && \
  apt-get install --no-install-recommends -y

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python -m src.bot"]