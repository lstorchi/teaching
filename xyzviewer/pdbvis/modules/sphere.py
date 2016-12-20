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

from point import *

class atom:

  def __init__(self, center, radius, number, name = ""):
    self._center = center
    self._radius = radius
    self._name = name
    self._number = number 

    self._sfo_list = [] # tutti gli sfo centrati in questo atomo

    self._mo_number = []
    self._mo_energy = []
    self._mo_percentage = []


  def set_center (self, center):
    self._center = center


  def set_radius (self, radius):
    self._radius = radius


  def set_name (self, name):
    self._name = name


  def set_number (self, number):
    self._number = number


  def get_number (self):
    return self._number


  def get_name (self):
    return self._name


  def get_center (self):
    return self._center


  def get_radius (self):
    return self._radius


  def get_volume (self):
    V = (4.0 / 3.0) * math.pi * math.pow(self._radius, 3)

    return V

  def is_point_inside (self, x, y, z):
    p = point(x, y, z)

    d = self._center.get_distance_from(p)

    return (d < self._radius)
