FROM python:3.8
MAINTAINER robert1003

WORKDIR /python/src/app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
