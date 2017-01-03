class atom(object): # nuovo stile di classe python subclass di object 
  def __init__(self, at, x, y, z):
    self.simbolo = at
    self.coordinate = (x, y, z)
  
  def set_symbol(self, at): 
    self.simbolo = at
  
  def get_symbol(self):
    return self.simbolo

  def set_coordinates(self, x, y, z):
    self.coordinate = (x, y, z)

  def get_coordinates(slef):
    return self.coordinates

  def get_str(self):
    return '%s %10.4f %10.4f %10.4f' % (self.simbolo, self.coordinate[0], \
        self.coordinate[1],self.coordinate[2])

  def __repr__(self): # overloads printing
    return self.get_str()

class molecule(object):
  def __init__ (self, nome = "noname"):
    self.name = nome
    self.lista_atomi = []

  def add_atom (self, atom):
    self.lista_atomi.append(atom)

  def get_atoms (self):
    return self.lista_atomi

  def __repr__ (self):
    str = 'Molecule %s\n' % self.name
    str = str + 'ha %d atomi\n' % len(self.lista_atomi)
    
    for atom in self.lista_atomi:
     str = str + atom.get_str() + '\n'

    return str
