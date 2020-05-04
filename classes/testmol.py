import mol

m = mol.molecule("metano")
a = mol.atom("C", 3.875, 0.678, -8.417)  
m.add_atom(a)
a = mol.atom("H", 3.800, 1.690, -8.076)  
m.add_atom(a)
a = mol.atom("H", 4.907, 0.410, -8.516)  
m.add_atom(a)
a = mol.atom("H", 3.406, 0.026, -7.711)  
m.add_atom(a)
a = mol.atom("H", 3.389, 0.583, -9.366)  
m.add_atom(a)

print(m)

