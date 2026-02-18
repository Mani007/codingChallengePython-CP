# calling c++ function in python
# Generate the .so or shared object file from C using the command below
# gcc -fPIC -shared -o clibpy.so clibpy.c
import ctypes
# Source - https://stackoverflow.com/a/3133594
# Posted by the_void
# Retrieved 2026-02-18, License - CC BY-SA 2.5


cimport = ctypes.CDLL("E://Document backup//codingChallengePython-CP//c++python//clibpy.so") 
cimport.display(b"AA",2) # converting string into binary string