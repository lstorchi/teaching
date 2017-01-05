import vtk
import sys 
import re

actors = []

source1 = vtk.vtkSphereSource()
source1.SetCenter(0.0, 0.0, 0.0)
source1.SetRadius(2.0)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
  mapper.SetInput(source1.GetOutput())
else:
  mapper.SetInputConnection(source1.GetOutputPort())
 
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.1, 0.1) # RGB
actor.GetProperty().SetOpacity(0.9)
actors.append(actor)

source2 = vtk.vtkCubeSource()
source2.SetCenter(3.0, 0.0, 0.0)
source2.SetXLength(2.0)
source2.SetYLength(2.0)
source2.SetZLength(2.0)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
  mapper.SetInput(source2.GetOutput())
else:
  mapper.SetInputConnection(source2.GetOutputPort())
 
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.2, 0.1, 1.0) #(R,G,B)
actor.GetProperty().SetOpacity(0.9)
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
