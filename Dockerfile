FROM python:3.10

WORKDIR $goit-algo-hw-08


COPY . .

EXPOSE 5000

ENTRYPOINT [ "python", "main.py"]