# NEEDS A REVIsion, translation and a formating into md for real

Nota:
Ver la carpeta docs la cual posee el approach con el que se diseño el trabajo, explicaciones sobre la toma de deciciones, propuestas de mejoras, e información del problema original


Instrucciones: (EXPLICAR LA NOMENCLATURA A USAR EN LOS ARCHIVOS, DAR EJEMPLOS)
    configFile.ini: (paths relativos al root directory!)

    Archivo de entrada:
        Payment data:
            Solo se ofrece una forma de input (debido a que este siempre debería ser relativamente corto)
        Employees data:
            Si una persona trabaja en más de un intervalo el mismo día, debera re indicarse el día para cada intervalo de trabajo (Ex: txt -> JUAN=MO10:00-12:00,MO14:00-16:00 ; json -> "JUAN":{ MO: ["10:00-12:00","14:00-16:00"]})
            Las horas pueden introducirse en formato de HH / HH:MM / HH:MM:SS, pero solo las horas son usadas para establecer los intervalos (se asume que no se puede iniciar un turno a cualquier horario, y que solo se puede iniciar un turno a la hora en punto como uno esperaría normalmente)
            Pueden usarse nombres cuyos caracteres se encuentren dentro del encode utf-8
            Los espacios y mayusculas puede usarse como uno quiera mientras se ingrese con el formato adecuado. Ex txt -> Juan = Mo 10 - 12:00 va a funcionar
        

Aclaraciones:
    Archivos de salida:
        Los resultados se imprimen en consola pero también se escriben dentro de la carpeta Output con el nombre de la fecha y hora de finalización del la corrida.
        Los nombres se pasan a mayúsucla en el código (porque asi era el ejemplo en el email, si no era la idea solo hay que eliminar .upper() en la clase lectora).
        
Bugs:
    JSON files doesn't like non-ASCII characters, so the output file will skip them when writing in this particular format