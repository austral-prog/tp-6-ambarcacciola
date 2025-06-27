def remove_elements(lista):
  nueva_lista = lista[:]
  for i in [5, 4, 0]:
   if len(nueva_lista) > i:
     del nueva_lista[i]
  return nueva_lista

def add_elements(lista):
  agregados = lista[:]
  agregados.append("Yellow")
  agregados.insert(0, "Pink")
  return agregados

def is_empty(lista):
  if lista == []:
    return True
  else:
    return False

def check_lists(lista1, lista2):
  if len(lista1) and len(lista2) > 3:
    if lista1[2] == lista2[2]:
      return True

  else: 
    return False

def list_of_lists(lista):
  nueva_lista = [
      lista[0][:2],    
      lista[1][0:4],    
      lista[2][-2:]     
  ]
  return nueva_lista
