FROM python:3.7-stretch

COPY main.py requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]

