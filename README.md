# distribuidosProyecto



## Getting Started

La macro-estructura del proyecto se va a dividir en diferente subproyectos catalogados en las siguientes categorias:

Ejecutables:
-   LacusCloud_consoleClientTest
-   LacusCloud_nodeServer (middleware)

No ejecutables:
-   lacusCloud_client (middleware)
-   lacusCloud_common (middleware)

Ejecutables de prueba que no aportan nada al proyecto final :v
-   lacusCloud_p2pClientTest

La idea es que un usuario externo pueda importar el codigo del lacusCloud_client, y asi acceder de forma transparente a los recursos de la red de nodos con solo configurar la IP del Servidor-Tracker.


Cada uno de los subproyectos siguen un patron de diseño definido de la siguiente manera:

![alt text](https://raw.githubusercontent.com/tavog96/distribuidosProyecto/master/doc/scheme.PNG)

-   No se utilizaran entidades hasta el momento, ya que es mas facil tratar los datos como arrays json. hasta que se implemente la autenticacion de usuarios, no veo necesario estos.

-   Core: Definie toda la logica de negocio, en termino de este proyectos, seria logica de procesamiento de datos de recursos, por ejemplo, evitar que se descargue un recurso que ya existe localmente. Es ignorante de los terminos de infraestructura.
-   Use Case: Define todas y cada una de las solicitudes que debe procesar la aplicacion, desde retornar una lista de recursos, hasta compartir uno de estos. Este debe ser un codigo reutilizable, fijo, y de cierta manera stateless, siendo cada solicitud completamente independiente de las otras, de manera que la Implementacion pueda instanciar cuantas Use Cases como quiera, permitiendo a la Implementacion hacer un uso "desechable" de estas instancias, por ejemplo; instanciando una nueva de estas en cada nueva solicitud.
-   Interfaces: Conocidos como repositorios, son interfaces o esqueletos de los diferentes metodos o servicios que la logica puede acceder hacia los servicios de infraestructura.
-   Helpers: Comunmente conocida como logica de definicion, o logica adicional, es por ejemplo, funciones para determeninar la igualdad de 2 recursos, y si un mismo recurso se repite en un lista.
-   Infrastructure: Compuesta por la logica de acceso a los servicios externos al sistema, como acceso a archivos, a otras APIs web, bases de datos, etc.
-   Controller: Conocido como Implementacion de Repositorio, constituye la implementacion de un servicio completo de acceso a datos externos, ya sea una API, un archivo, una coleccion de recursos, etc. Normalmente heredan de las Interfaces del core, para asegurarse de que se cubran todos los metodos y funciones requeridas por la logica del core y los Uses Cases.
-   Controller Logic: Logica adicional utilizada por los Controller, por ejemplo, para trasfornar la data recibida a un formato estandar para la logica, para evitar recibir data corrupta, erronea, incongruente.
-   Implementation: Seccion unica de los proyectos ejecutables, implementa la logica como parte de una interfaz de acceso, bien local (Consola), bien interfaz web (API), para que el usuario acceda a estos procesos, ademas, define (o lee de un archivo, o ambas) las variables de configuracion del entorno de ejecucion, como por ejemplo: El path de una carpeta de descargas, la IP del servidor local, la IP del servidor remoto, si se debe comportar como simple nodo, o como tracker central, etc.
-   Runtime config: Logica que ayuda a definir, guardar y compartir entre procesos locales, las variables de configuracion del entorno de ejecucion, ya sea a travez de un archivo, de variable global, etc. Dandole posibilidad al usuario de modificar estas variables.
-   Access Interface: Ejecucion de la interfaz implementada para recibir solicitudes del usuario, ya sea por una interfaz grafica, una consola, una restAPI, un WebService, una App Android, loque sea :v.
-   Use Case: Uso adecuado de los Use Case disponibles en el Core, uso desechable, para cada una de las solicitudes recibidas por el Access Interface, y segun las variables del Runtime Config (Las variables de configuracion de entorno de ejecucion pueden modificar el comportamiento de la implementacion).
-   Controllers: Uso de desechable, inicializados y configurados para cada una de las solicitudes que el Acces Interface asi requiera, los Controllers deben ser inicializados acuerdo a los parametros del Runtime config, osea, por ejemplo, configurar la direccion de la carpeta de desacagas para el cotrolador que se encargue de manipular estos archivos. Una vez inicializados, se le asginan (inyectan) los controllers ya configurados a los Use Cases, para que estos los utilicen en vez de las Interfaces. De manera que la capa de Implementacion siempre tenga control de que Logica y que Controllers se utilizan en cada solicitud que se procese.



### Prerequisites

require [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - The web framework used as server

### Installing

Easy peasy

## Running the tests

Ejecucion de prueba en la direccion: lacusCloud_middleware/lacusClient_p2pClientTest/main.py
Then just go http://localhost:5000/resource

### Break down into end to end tests

aun nada aca

### And coding style tests

Aun no se ha propuesto el fromato de la codificacion de pruebas

## Deployment

Nada que ver aca, si nos sirve en el aula ganamos mucho mas bien :v

## Built With

* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - The web framework used as server
* [Motivational-memes](https://www.youtube.com/watch?v=yCWSeBuaybc)

## Contributing

None existing yet

## Versioning

[Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) maybe idk

## Authors

* **Villa** - *Coder 1* -
* **ROD** - *Coder 2* -
* **TOBBY** - *Coder 3* - 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration (What is supposed to be written here?)
* etc
