FROM python:3.7-stretch

WORKDIR /app
COPY endpoints_server.py requirements.txt endpoints_pb2_grpc.py endpoints_pb2.py /app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "endpoints_server.py"]

