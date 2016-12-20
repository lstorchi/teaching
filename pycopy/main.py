
###############################################################################

class Aclass:

  def __init__ (self):
    self._a = 0

  def setb (self, bin):
    self._b = bin

  def seta (self, ain):
    self._a = ain

  def geta (self):
    return self._a

  def getb (self):
    return self._b

###############################################################################

a = Aclass ()

a.seta(1)

# try to comment this
a.setb(1)
#

b = a

print b.geta(), b.getb()

