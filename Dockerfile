FROM python:3
WORKDIR /usr/src/shp
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/shp
EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#сборка контейнера 
#docker build -t shd .
#команда для запуска
#docker run --name shop -p 8000:8000 -d shd
