FROM tiangolo/meinheld-gunicorn:python3.7

WORKDIR /app/
ADD . /app/

# uWSGI will listen on this port
EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt
# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=DReport.deploy

ENV APP_MODULE="DReport.wsgi"
ENV GUNICORN_CONF="/app/DReport/gunsetting.py"

# CMD ["gunicorn","-c","DReport/gunsetting.py","DReport.wsgi"]