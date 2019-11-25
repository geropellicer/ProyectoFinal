FROM python:3.7.5-alpine

EXPOSE 8080

# Crear la carpeta donde clonamos el proyecto
WORKDIR /home/
RUN mkdir project

RUN apk update \
	&& apk add npm

WORKDIR /home/project/frontend

COPY ./frontend .

WORKDIR /home/project/frontend

CMD ["npm", "run", "serve"]

