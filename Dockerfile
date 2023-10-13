FROM python:3.11

WORKDIR /app

COPY dependencies.txt .

RUN pip install -r dependencies.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["python", "manage.py", "runserver", "http://127.0.0.1:8000"]