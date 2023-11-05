FROM python:3.9

ENV DJANGO_SETTINGS_MODULE=store.settings
ENV DEBUG=False

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "store.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000
