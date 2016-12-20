import vtk
import sys 
import re

#####################################################################

def get_color (atom):

  if (atom == 'C'):
    return 1.0, 0.0, 0.0
  elif (atom == 'H'):
    return 1.0, 1.0, 1.0

  return 0.0, 0.0, 0.0

#####################################################################

filename = ""

radius = {'H':1.2, 'C':1.7}

if (len(sys.argv)) == 2:
  filename = sys.argv[1]
else:
  print "usage :", sys.argv[0] , " xyzfile"
  exit(1)

filep = open(filename, "r")

filep.readline()
filep.readline()

actors = []

for line in filep:
  p = re.compile(r'\s+')
  line = p.sub(' ', line)
  line = line.lstrip()
  line = line.rstrip()

  plist =  line.split(" ")

  if (len(plist) == 4):
   atomname = plist[0]
   x = plist[1]
   y = plist[2]
   z = plist[3]

   if atomname in radius:
     print atomname, " has ", radius[atomname], x, y, z

     source = vtk.vtkSphereSource()
     source.SetCenter(float(x),float(y),float(z))
     source.SetRadius(radius[atomname])

     mapper = vtk.vtkPolyDataMapper()
     if vtk.VTK_MAJOR_VERSION <= 5:
       mapper.SetInput(source.GetOutput())
     else:
       mapper.SetInputConnection(source.GetOutputPort())
                 
     actor = vtk.vtkActor()
     actor.SetMapper(mapper)
     actor.GetProperty().SetColor(get_color(atomname)); #(R,G,B)
     actors.append(actor)


filep.close()

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
