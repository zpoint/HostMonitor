FROM python:3.7-alpine
WORKDIR /HostMonitor
RUN apk add --update alpine-sdk
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py", "--env=local"]
