FROM python:3.7.5-alpine

EXPOSE 8000

# Crear la carpeta donde clonamos el proyecto
WORKDIR /home/
RUN mkdir project

WORKDIR /home/project

COPY . .

RUN pip install -r requirements.txt \
	&& python manage.py makemigrations \
	&& python manage.py migrate

WORKDIR /home/project/

ENTRYPOINT [ "python", "manage.py" ]
CMD ["runserver", "0.0.0.0:8000"]

#Debe ejecutarse con -v $(pwd):/home/project/