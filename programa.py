import clases as IC

#Prueba básica de funcionamineto de la parent class a las demás clases que heredaron, solamente los atributos definidos
ALU= IC.ALU()
print(ALU.Add())
print(ALU.Sub())
print(ALU.BSO())

RAM = IC.Memory()
print(RAM.purpose)
print(RAM.data)

