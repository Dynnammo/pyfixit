# -*- coding: utf-8 -*-
import requests

from base import Base
from constants import API_BASE_URL

class Image(Base):
   def __init__(self, id):
      self.id = id
   
   def __str__(self):
      return self.name # FIXME
   
   def __repr__(self):
      return '<Image %s>' % self.id
   
   def __eq__(self, other):
      if not isinstance(other, Image):
         return false
      
      return self.id == other.id
   
   def refresh(self):
      response = requests.get('%s/media/images/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      #self.exif = attributes['exif']
      self.height = attributes['height']
      self.width = attributes['width']
      #self.ratio = attributes['ratio']
      #self.markup = attributes['markup']
      #self.srcid = attributes['srcid']
      
      image = attributes['image']
      # Images are allowed to have different sizes, depending on the dimensions
      # of the original image.  To avoid doing a bunch of explicit 'in' checks,
      # splat the variables into scope.
      del(image['id'])
      for size in image:
         vars(self)[size] = image[size]
