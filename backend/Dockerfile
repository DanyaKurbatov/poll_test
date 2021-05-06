FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /backend

COPY . /backend/.

WORKDIR /backend

RUN ls .

#RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

VOLUME /backend

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

