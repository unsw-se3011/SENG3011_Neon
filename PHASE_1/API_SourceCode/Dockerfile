FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV  DJANGO_SETTINGS_MODULE "DReport.deploy"
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000

CMD [ "./manage.py","runserver","0.0.0.0:8000" ]