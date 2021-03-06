#### Archivo que explica las diferentes propuestas consideradas para cada clase nombrada en Approach.txt y la razon de porque se eligio una sobre la otra

---

## Container Payments (diferentes opciones al almacenamiento de data):
- Cada día con 24hs explicitas: {MO:{0:25, 1:25, ..., 23:20}, TU:{...}, ...}
    - Pros:
        - Todo se trabaja como diccionario -> Extremadamente rápido O(1)
        - 7d*24h -> Voy a tener un máximo de 343(7d+168hs+168costos) entradas en memoria (extremadamente barato a nivel memoria. Para el caso no tiene sentido considerar otras maneras de almacenar en memoria para ahorrar espacio)
        - Trabajar de esta forma brinda un fácil acceso a los datos para los clases que los requiren
        - Trabajar de esta forma facilita enormemente como realizar los calculos a posteriori (se busca la hora, se saca el precio, y se lo suma en un auxliar. Fin de la historia)
    - Cons:
        - No se aplica al caso particular, pero en un caso de mayor tamaño, esto no seria posible de aplicar debido a los costos de memoria invertidos en datos innesarios (Además de que los diccionarios son más pesados que por ejemplo trabajar con una lista y usar las horas como indice de acceso como una alternativa más liviana)

    - Alternativa equivalente:
        - Se podría trabajar con listas:Ejemplo: {MO:[25, 25 ..., 20, 20], TU:[..., ...], ...} 
            - Pros:
                - Esto permite usar las horas como indices de acceso
                - Seria un equivalente a los diccionarios sin tener que gastar costos de memoria en hash (Pero sigue teniendo almacenamiento de datos que podrían evitarse)
            - Cons:
                - Lo considero un poco más obscuro a nivel código (dificulta un poco el entender el almacenamiento y el acceder a la memoria) 
        


- Cada día con arrays de intervalos y costos [start, finish, cost]: {MO:[[0,9,25], [9,18,15], [18,0,20]], TU:[[...], ...], ...}
    - Pros:
        - Evito almacenar datos innecesarios al trabajar con intervalos (Sería una forma mucho mejor de trabajar en un caso mucho más grande donde la memoria importe).
            - Para el caso particular:
                - Mejor caso: 7d con mismo pago en cada horario -> 7 dias + 21 elementos (7 instancias de 1 array de 3 elementos) = 28 entradas
                - Peor caso: 7d donde cada hora tiene un pago distinto -> 7 dias + 7 * 72 (7 instancias de 24 arrays de 3 elementos) = 511 entradas
        - Esperaría siempre caer en situaciones similares al mejor caso, donde hay pocos intervalos diarios de variación
        - Se puede usar la libreria interna datetime para trabajar los intervalos
            - Especificamente la clase timedelta para conseguir las horas que tenemos entre intervalos

    - Cons:
        - Más obscuro al leerlo y trabajarlo que la opción de puros diccionarios sin una verdadera ganancia
        - Necesito un sistema que reconozca en que intervalo estoy trabajando (el sistema debería checkear buscando hora de entrada comprendida entre 2 start y una hora de salida comprendida entre dos finish)
            - Este sistema debe ser capaz de detectar intervalos que se cruzan y saber que horas corresponden a cada uno
        - Trabajo con listas asi que las busquedas de intervalos van en orden de O(n)
        - Dificilmente se caiga en un caso malo de almacenamiento donde se ocupe más memoria que en el caso de diccionarios, pero la posibilidad existe y debe tenerse en cuenta
    
- Diccionario (días) -> Diccionario (horas del dia en array) -> [Array formado por range(start,end)] (Se debe tener cuidado con el caso donde se pasa de 23 horas en adelante!) : cost
    - La idea es checkear los keys de cada día (arrays con los valores abarcados por el intervalo), y  ver si la hora buscada esta dentro del array con in
    
    - Pros:
        - Más eficiente en memoria que el sistema de puros diccionarios (no repito los costos para cada hora, solo se guarda uno por intervalo)
        - Más amigable que el sistema de [start, finish, cost] pero menos que el sistema diccionario
    
    - Cons:
        - Menos eficiente computacionalmente que el sistema de diccionarios
        - Menos eficiente en memoria que el sistema [start, finish, cost]


**Elección**: Debido a la simplicidad del problema, no se considera necesario buscar optimización de memoria ni de computo. Bajo esa premisa se elige aquel que de la presentación entendible y fácil de manegar del código, por lo que se elige la opcion de puros diccionarios

---

## Container Employees:
  * Una lista donde cada elemento es un array conformado por el nombre del empleado y por un diccionario compuesto por la estructura {\<day>: [\<start>, \<finish>]}
      - Ex: [['Pedro', {'MO':[0,4],'TU':[0,4], ...}], ['Juan', {'MO':[0,4],'TU':[0,4], ...}], ...]
      - No hay riesgo de sobreescribir los datos de un empelado en caso de que más de uno compartan el nombre
      - Puedo usar los indices en la lista como ids
      - Como tengo que recorrer 

    
  * Usar un diccionario que directamente enlace los nombres con los horarios tiene el problema de que va a reescribir los datos si los nombres se comparten
      - Evitar ese problema por medio de ids o un sistema equivalente es posible pero pareceria matar la gracia de usar el diccionario al complejizar la estructura
      - Otro problema del diccionario es el orden de recorrido. Preferiblemente me gustaria un output en el mismo orden de entrada para facilitar la lectura y eso solo podría hacerlo empleando collections -> OrderedDict (complejizo aun más siendo que la lista por default me da este comportamiento).


  * No tiene sentido considerar otra estructura pues la letura va a hacerse linea por linea y agregando los contenedores, por lo que necesito objetos mutables eliminando posibilidad de tuplas, y sets no tienen sentido en este problema

**Elección**: Sistema 

---

## Lectura y conversion:
- Lectura se realiza sobre archivos establecidos en el codigo o desde la misma consola. 
- La lectura de payments y employees asumen escritos bajo los formatos planteados al inicio de este archivo.
- La lectura de los payments solo se realiza en formato json debido a que escribir algo como debería ser un suceso raro y a la vez de nos más de unos minutos.
    
- Se propone un builder que de acuerdo a un archivo de configuración decida que formato de input instanciar y usar para leer.

---

**Formatos de lectura esperados**:
  - LecturaPaymentes(json): \<Dia>=[[\<start> - \<finish>, \<cost>, ...]
  - LecturaEmployees(json y txt): \<Empleado>=\<day>\<start>-\<finish>, ...

---

## Calculation:
  - Debido al formato de container seleccionados para trabajar, los pasos para esta clase deberian ser:
      - Recibir el container de payments y de empleados sobre los que calcular
      - Usar un contador para acumular lo que cada empleado gana por hora
      - Recorrer cada intervalo y acumular las ganancias por horas trabajadas
      - Retornar un arreglo con el formato \<index>-\<name>: \<pay> \<currency>

---

## Writer:
  - Debe imprimir en consola
  - Debe asegurarse que la carpeta Output existe
  - Debe crear y escribir el archivo output con nombre de la fecha-hora actual