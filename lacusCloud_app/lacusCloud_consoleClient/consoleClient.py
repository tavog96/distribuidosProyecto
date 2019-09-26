"""
En terminos basicos, el consoleCliente sera el cliente de consola que se encargara de importar
los paquetes middleware del lacusCloud_client para acceder a los servicios de la red distribuida.
El cliente solo debera tener acceso y uso de las funciones:

    * Obtener lista de los recursos disponibles en la red de nodos (con sus UID).
    * Descarga de un recurso (por su UID).
        * Consultar porcentaje de descarga.
        * Consultar velocidad de descarga.
    * Compartir un recurso (Pasando la direccion del recurso en el Disco Duro)
    * Establecer la dirección de una carpeta de descargas
    * Establecer IP local del cliente.
    * Establecer IP del servidor Tracker.
    * Establecer si el cliente comparte recursos con otros nodos o no.

La implementacion del middleware lacusCloud_client debe ser limpia, de manera que desde este cliente de consola
que emula una implementacion real del packete middleware (como si fuese un ambiente de producción),
no se debe tener acceso, y debe ser completamente ajeno a:

    * Direcciones IP de otros nodos.
    * Cantidad o configuracion de los chunks de los recursos.
    * Cantidad de nodos.
    * Cantidad de 


"""