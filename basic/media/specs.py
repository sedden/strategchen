from imagekit.specs import ImageSpec 
from imagekit import processors 

class ResizeThumb(processors.Resize): 
    width = 460
    #height = 306
    crop = False

class ResizeDisplay(processors.Resize):
    width = 1024

class EnchanceThumb(processors.Adjustment): 
    sharpness = 1.1 

class Thumbnail(ImageSpec): 
    pre_cache = True 
    processors = [processors.Transpose, ResizeThumb, EnchanceThumb] 

class Display(ImageSpec):
    processors = [processors.Transpose, ResizeDisplay]
