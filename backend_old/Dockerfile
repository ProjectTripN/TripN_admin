
FROM python:3.8-slim-buster AS builder
ADD . .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","-m","unittest","discover","-s","tests"]