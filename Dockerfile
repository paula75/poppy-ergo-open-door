FROM python:3.5


RUN apt-get update && apt-get install -y \
    python-pip

RUN pip install requests


WORKDIR /app
COPY . /app

CMD ["python", "src/api.py"]
