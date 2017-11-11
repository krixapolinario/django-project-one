FROM python:3.6.3

WORKDIR /usr/src/

COPY src/ ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/projectone/

RUN python manage.py startapp oficina

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
