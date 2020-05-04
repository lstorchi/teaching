import mol
import vtk

m = mol.molecule("metano")
a = mol.atom("C", 3.875, 0.678, -8.417)  
a.set_radius(1.7)
a.set_color(1.0, 0.0, 0.0)

m.add_atom(a)
a = mol.atom("H", 3.800, 1.690, -8.076)  
a.set_radius(1.2)
a.set_color(1.0, 1.0, 1.0)
m.add_atom(a)

a = mol.atom("H", 4.907, 0.410, -8.516)  
a.set_radius(1.2)
a.set_color(1.0, 1.0, 1.0)
m.add_atom(a)

a = mol.atom("H", 3.406, 0.026, -7.711)  
a.set_radius(1.2)
a.set_color(1.0, 1.0, 1.0)
m.add_atom(a)

a = mol.atom("H", 3.389, 0.583, -9.366)  
a.set_radius(1.2)
a.set_color(1.0, 1.0, 1.0)
m.add_atom(a)

print(m)

actors = []

for a in m.get_atoms():
  source = vtk.vtkSphereSource()
  source.SetCenter(a.get_coordinates()[0], \
      a.get_coordinates()[1],  a.get_coordinates()[2])
  source.SetRadius(a.get_radius())

  mapper = vtk.vtkPolyDataMapper()
  if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(source.GetOutput())
  else:
    mapper.SetInputConnection(source.GetOutputPort())
 
  actor = vtk.vtkActor()
  actor.SetMapper(mapper)
  actor.GetProperty().SetColor(a.get_color()[0], a.get_color()[1], a.get_color()[2]) 
  actor.GetProperty().SetOpacity(1.0)
  actors.append(actor)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
for actor in actors :
  ren.AddActor(actor)
                
iren.Initialize()
renWin.Render()
iren.Start()
