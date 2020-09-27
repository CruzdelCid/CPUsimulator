#Primer approach a decoder para poder detectar instrucción válida e inválida
#array asociativo
instrucciones={}
instrucciones['0000']='0000'
instrucciones['OUT']='0000'
instrucciones['OUTPUT']='0000'
instrucciones['0001']='0001'
instrucciones['LOAD_R0']='0001'
instrucciones['LD_R0']='0001'

#en el momento de leer la linea a ejecutar (lines)
#una idea es usar instrucciones en un array asociativo para poder 
#por un split encontrar las partes de la linea, y obtener el comando en lenguaje
#maquina

current_line='LOAx_R0 14' ## ejemplo de una linea
#decode
#CU.decode(current_line)  por implementar en metodo decode
current_parts=str.split(current_line)
comando=current_parts[0]
try:
   instruccion_a_ejecutar = instrucciones[comando]
except KeyError:
   instruccion_a_ejecutar=None
   print('ERROR: comando invalido' )

#instrucciones[str.split(current)[0]]
print(instruccion_a_ejecutar)

current_line='LOAD_R0 14' ## ejemplo de una linea
#decode
#CU.decode(current_line)  por implementar en metodo decode
current_parts=str.split(current_line)
comando=current_parts[0]
try:
   instruccion_a_ejecutar = instrucciones[comando]
except KeyError:
   instruccion_a_ejecutar=None
   print('ERROR: comando invalido' )

#instrucciones[str.split(current)[0]]
print(instruccion_a_ejecutar)