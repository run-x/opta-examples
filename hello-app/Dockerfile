FROM python:3.8-slim-buster

ENV FLASK_APP=app

WORKDIR /app

RUN pip install Flask==0.12 
COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
