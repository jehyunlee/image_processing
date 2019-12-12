from java.lang import Character, Byte, Short, Integer, Long, Float, Double, Boolean
from java.lang.reflect.Array import newInstance as newArray  
  
primitiveTypeClass = {'c': Character, 'b': Byte, 's': Short, 'h': Short, 'i': Integer, 'l': Long, 'f': Float, 'd': Double, 'z': Boolean}  

def nativeArray(stype, dimensions):
    """ Create a native java array such as a double[3][4] like: 
    arr = nativeArray('d', (3, 4)) 
    In other words, trivially create primitive two-dimensional arrays 
    or multi-dimensional arrays from Jython. 
    Additionally, if dimensions is a digit, the array has a single dimension. 
 
    stype is one of: 
    'c': char 
    'b': byte 
    's': short 
    'h': short (like in the jarray package) 
    'i': integer 
    'l': long 
    'f': float 
    'd': double 
    'z': boolean 
    """  
    return newArray(primitiveTypeClass[stype].TYPE, dimensions)

print nativeArray('b', (10))