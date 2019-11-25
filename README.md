# Proyecto Django + Vue.js

##### Este proyecto es una prueba de concepto pero también un arquetipo listo para utilizarse, del stack Django como Backend (en este caso por defecto utiliza la versión 2.1.11 pero puede ser modificado)  Vue.js como frontend (en este caso utiliza la versión 2.6.6 pero también puede ser modificado).

##### Entre las principalesa características de este proyecto se encuentran que está listo para ser utilizado de inmediato con Docker y que a su vez se presenta en dos versiones pensadas para desarrollo y producción respectivamente. Ambas están dockerizadas pero con diferentes métodos pensadas para facilitar enormemente el desarrollo utilizando este stack. Describimos a continuación las dos variantes.

***

## Local Testing
#### Esta versión consiste de dos imágenes Docker que se levantan por separado (una para el frontend y otra para el back) con la particularidad de que se usa un bind-mount a la carpeta de desarrollo local. Esto, en conjunto con una técnica que utilizamos de [este curso](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/), **permite usar hot reload para el back y para el front al mismo tiempo**. La combinación del bind mount que prooponemos y la técnica de hot reload doble permiten un entorno muy cómodo para desarrollar en el que ambos servidores de desarrollo (de Django y de NPM-Vue) se levantan con un solo comando de Docker, en donde cualquier cambio que hagamos a nuestros archivos locales se refleja directamente dentro del contenedor y en donde cualquier cambio persiste, es decir, se puede parar el contenedor, levantarlo de nuevo mañana y continuar por donde dejamos con todos los cambios guardados.


### Instrucciones

#### Prerequisitos
Python >=  3.6
Node >= 10
NPM >= 6
Docker CE >= 19

#### Clonar el repositorio
En una carpeta local que seleccionemos para trabajar, abrir una terminal y hacer git clone de este repositorio

#### Buildear las imágenes de Docker
Dentro de la carpeta que se nos crea cuando clonamos el repositorio, tenemos que buildear la imagen para levantar con Docker el Front y el Backend.

```Docker
docker image build -t frontvue . -f front.Dockerfile
docker image build -t backdjango . -f back.Dockerfile
```

#### Levantar los contenedores de Docker
```Docker
docker container run -d -p 80:8000 -v $(pwd):/home/project/ backdjango
docker container run -d -p 8080:8080 -v $(pwd):/home/project/ frontvue
```

Así como está, por defecto expone los puertos locales 80 y 8080 y los mapea con los puertos necesarios de los contenedores de Docker. Si por alguna razón tenemos alguno de estos puertos locales, se puede cambiar  especificar otro. Por ejemplo para exponer nuestro puerto 8888 para el backend haríamos "-p 8888:8000" y en lugar de ir luago a "localhost" iríamos a "localhost:8888". 


#### Todo listo
Ya se puede visitar <localhost> (ó <localhost:puerto-del-backend> si hemos especificado un puerto distinto en el contenedor del backend).

Para comprobar que todo está funcionando, podemos hacer cualquier cambio en los archivos de nuestra carpeta local (sea en el Front o en el Back) y se deberían reflejar automáticamente.

Adicionalmente, si se desea ver los logs de cada contenedor, se pueden correr los comandos "docker container run" sin la opción "-d", cada uno en una terminal distinta.

Los contenedores se puede parar y volver a levantar, o incluso para y borrar, y los cambios deberían persistir en nuestra carpeta de trabajo local.

*** 



## Production
#### 