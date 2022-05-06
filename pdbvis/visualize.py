#
# Loriano Storchi this file is part of teaching repo 
# 
# teaching is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

import re
import vtk
import sys
import math
import numpy

sys.path.append("./modules")

import sphere
import point

###############################################################################

class vtkTimerCallback():
  def __init__(self):
    self.timer_count = 0
         
  def execute(self,obj,event):

    iren = obj
    wren = iren.GetRenderWindow()
    renderer = wren.GetRenderers().GetFirstRenderer()

    #print renderer.GetActiveCamera().GetFocalPoint()
    #print renderer.GetActiveCamera().GetPosition()

###############################################################################

RTI = 0.7
GTI = 0.7
BTI = 0.7

SRTI = 0.7
SGTI = 0.68
SBTI = 0.65

RO = 0.8
GO = 0.5
BO = 0.5

SRO = 0.5
SGO = 0.3
SBO = 0.3

RH = 1.0
GH = 1.0
BH = 1.0

SRH = 1.0
SGH = 0.78
SBH = 0.65

def atomname_to_rgb (name):

  if (name == "C"):
    return RTI, GTI, BTI, SRTI, SGTI, SBTI
  elif (name == "O"):
    return RO, GO, BO, SRO, SGO, SBO
  elif (name == "H"):
    return RH, GH, BH, SRH, SGH, SBH
  
  return 0, 0, 0, 0, 0, 0

def position_to_rgb (x, y, z):

  if ((z < (18.7 + 4.0)) and (z > (18.7 - 4.0))):
    return 1.0, 0.0, 0.0

  return 0.0, 0.0, 1.0

###############################################################################

def read_pdb_limits (filename):

  xmin = ymin = zmin =  1000000.0
  xmax = ymax = zmax = -1000000.0

  pdbfp = open(filename, "r")

  for str in pdbfp:
    str = str.lstrip(" \t\n\r")
    str = str.rstrip(" \t\n\r")
    str = re.sub(' +',' ', str)

    plist = str.split(" ")

    if (plist[0] == "HETATM"):
      x = float(plist[5])
      y = float(plist[6])
      z = float(plist[7])
      
      if (x > xmax):
        xmax = x
      if (y > ymax):
        ymax = y
      if (z > zmax):
        zmax = z

      if (x < xmin):
        xmin = x
      if (y < ymin):
        ymin = y
      if (z < zmin):
        zmin = z

  pdbfp.close()

  return xmin, xmax, ymin, ymax, zmin, zmax

###############################################################################

def append_atom_using_file (actors, pdbfilename):

  pdbfp = open(pdbfilename, "r")

  for str in pdbfp:
    str = str.lstrip(" \t\n\r")
    str = str.rstrip(" \t\n\r")
    str = re.sub(' +',' ', str)

    plist = str.split(" ")

    if (plist[0] == "ATOM"):
      atomname = plist[2]
      x = float(plist[5])
      y = float(plist[6])
      z = float(plist[7])

      r = 0.0
      if (atomname == "C"):
        r = 0.3
      elif (atomname == "O"):
        r = 0.3
      elif (atomname == "H"):
        r = 0.2

      source = vtk.vtkSphereSource()
      source.SetCenter(x, y, z)
      source.SetThetaResolution(16)
      source.SetStartTheta(0)
      source.SetEndTheta(360)
      source.SetPhiResolution(16)
      source.SetStartPhi(0)
      source.SetEndPhi(180)
      source.SetRadius(r)

      mapper = vtk.vtkPolyDataMapper()
      #mapper.SetInput(source.GetOutput())
      mapper.SetInputConnection(source.GetOutputPort())

      atom = vtk.vtkLODActor()
      atom.SetMapper(mapper)
      atom.GetProperty().SetRepresentationToSurface()
      atom.GetProperty().SetInterpolationToGouraud()
      atom.GetProperty().SetAmbient(0.15)
      atom.GetProperty().SetDiffuse(0.85)
      atom.GetProperty().SetSpecular(0.1)
      atom.GetProperty().SetSpecularPower(30)
      atom.GetProperty().SetSpecularColor(1, 1, 1)
      atom.GetProperty().SetOpacity(1.0)
      atom.SetNumberOfCloudPoints(30000)

      r, g, b, sr, sg, sb = atomname_to_rgb(atomname)
      atom.GetProperty().SetColor (r, g, b)
      atom.GetProperty().SetSpecularColor (sr, sg, sb)

      #r, g, b = position_to_rgb (x, y, z)
      #atom.GetProperty().SetColor (r, g, b)
      #atom.GetProperty().SetOpacity(0.7)

      actors.append(atom)

  pdbfp.close()

  return

###############################################################################

def append_bond_using_file(actors, pdbfilename):

  pdbfp = open(pdbfilename, "r")

  atomnamelist = []
  xlist = []
  ylist = []
  zlist = []

  for str in pdbfp:
    str = str.lstrip(" \t\n\r")
    str = str.rstrip(" \t\n\r")
    str = re.sub(' +',' ', str)

    plist = str.split(" ")

    if (plist[0] == "ATOM"):
      atomname = plist[2]
      atomnamelist.append(atomname)

      x = float(plist[5])
      xlist.append(x)

      y = float(plist[6])
      ylist.append(y)

      z = float(plist[7])
      zlist.append(z)

  pdbfp.close()

  pdbfp = open(pdbfilename, "r")

  bondSource = vtk.vtkCylinderSource()
  bondSource.SetRadius( 0.1 )
  bondSource.SetHeight( 1. )
  bondSource.SetResolution( 15 )
  bondSource.CappingOff()

  bondMapper = vtk.vtkPolyDataMapper()
  bondMapper.SetInputConnection(bondSource.GetOutputPort())

  for str in pdbfp:
    str = str.lstrip(" \t\n\r")
    str = str.rstrip(" \t\n\r")
    str = re.sub(' +',' ', str)

    plist = str.split(" ")
    if (plist[0] == "CONECT"):
      atoms = []
      atomsname = []
      for an in plist:
        if (an != "CONECT"):
          n = int(an) - 1
          print((n, xlist[n], ylist[n], zlist[n]))
          atoms.append(point.point(xlist[n], ylist[n], zlist[n]))
          atomsname.append(atomnamelist[n])

      for i in range(1,len(atoms)):
        direction = (atoms[i] - atoms[0])
        length = point.norm(direction)
        quarter = direction * ( 1.0 / 4.0)
        whereFrom = atoms[0] + quarter
        whereTo = atoms[i] - quarter
      
        # y-axis versor
        y_dir = point.point(0.0, 1.0, 0.0)
        # bond versor
        direction = direction * (1.0 / length)
        # get rotation axis
        rot_axis = direction + y_dir
        rot_axis = point.point(rot_axis.get_x() / 2.0, rot_axis.get_y() / 2.0, rot_axis.get_z() / 2.0)
        n = point.norm(rot_axis)
        rot_axis = point.point(rot_axis.get_x() / n, rot_axis.get_y() / n, rot_axis.get_z() / n)
      
        bondActor_from = vtk.vtkLODActor()
        bondActor_from.SetMapper( bondMapper )
        bondActor_from.SetPosition( whereFrom.get_x(), 
            whereFrom.get_y(), whereFrom.get_z() )
        bondActor_from.SetScale( 1., length/2, 1. )
        bondActor_from.RotateWXYZ(180., rot_axis.get_x(), 
            rot_axis.get_y(), rot_axis.get_z())
        r, g, b, sr, sg, sb = atomname_to_rgb(atomsname[0])
        #r, g, b = position_to_rgb (whereFrom.get_x(), whereFrom.get_y(), 
        #    whereFrom.get_z())
        bondActor_from.GetProperty().SetColor(r, g, b)
        bondActor_from.GetProperty().SetOpacity(0.7)
      
        actors.append(bondActor_from)
      
        bondActor_to = vtk.vtkLODActor()
        bondActor_to.SetMapper( bondMapper );
        bondActor_to.SetPosition( whereTo.get_x(), 
                                  whereTo.get_y(), 
                                  whereTo.get_z())
        bondActor_to.SetScale( 1., length/2, 1. )
        bondActor_to.RotateWXYZ(180., rot_axis.get_x(), rot_axis.get_y(), 
            rot_axis.get_z())
        r, g, b, sr, sg, sb = atomname_to_rgb(atomsname[i])
        #r, g, b = position_to_rgb (whereTo.get_x(), whereTo.get_y(),
        #    whereTo.get_z())
        bondActor_to.GetProperty().SetColor(r, g, b)
        bondActor_to.GetProperty().SetOpacity(0.7)
      
        actors.append(bondActor_to)

  pdbfp.close()

  return

###############################################################################


# create a rendering window and renderer
ren = vtk.vtkRenderer()
#ren.SetBackground(1,1,1)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

filename = "nanoparticle.pdb"

if (len(sys.argv)) == 2:
  filename = sys.argv[1]

xmin, xmax, ymin, ymax, zmin, zmax = read_pdb_limits (filename)

#pdb = vtk.vtkPDBReader()
#pdb.SetFileName(filename);
#pdb.SetHBScale(1.0);
#pdb.SetBScale(1.0);
#pdb.Update();
#print "# of atoms is: ", pdb.GetNumberOfAtoms()
 
actors = []

#append_bond(actors, pdb)
#append_using_vtk_pdb (actors, pdb)
append_bond_using_file(actors, filename)
append_atom_using_file(actors, filename)

for actor in actors:
  ren.AddActor(actor)

camera = vtk.vtkCamera ()

#camera.SetFocalPoint(13.32, 13.34, 34.2)
#camera.SetPosition(100.0, -103.014327654513146, 109.21120077738299)
#ren.SetActiveCamera(camera)

renWin.SetSize(1024, 768)
renWin.Render()

renderLarge = vtk.vtkRenderLargeImage()
renderLarge.SetInput(ren)
#renderLarge.SetInputConnection(ren)
renderLarge.SetMagnification(4)

camera = ren.GetActiveCamera()
#print ren.GetActiveCamera().GetPosition()

light = vtk.vtkLight()
#light.SetFocalPoint(camera.GetFocalPoint())
light.SetPosition(camera.GetPosition())

light.PositionalOn()
light.SetConeAngle(10.0)
light.SetIntensity(0.9)

ren.AddLight(light)

# enable user interface interactor
try:
  iren.Initialize()

  cb = vtkTimerCallback()
  iren.AddObserver('TimerEvent', cb.execute)
  timerId = iren.CreateRepeatingTimer(100);

  iren.Start()
except Exception as e:
  print(e)
