import yaml   ##para leer archivo de configuración

class Bios():
  def __init__(self,archivo_yaml):
    bios = yaml.safe_load(open(archivo_yaml))
    self.clock  = bios['clock']
    self.radix  = bios['visualization']['Radix']
    self.ram_data=bios['RAM']['data'] 
    self.ram_instructions=bios['RAM']['instructions'] 
    self.full = bios
