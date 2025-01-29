FROM python:3.10-slim

WORKDIR /app

ADD . /app/case1

WORKDIR /app/case1

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

CMD python ./src/manage.py migrate & python manage.py search_text & python ./src/manage.py collectstatic --no-input & python ./src/manage.py runserver 0.0.0.0:8000
