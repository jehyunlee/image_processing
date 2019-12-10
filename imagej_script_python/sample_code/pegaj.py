from os.path import join, isdir, isfile
import os, time, sys
# Add plugin folder to search path
#from java.lang.System import getProperty
modulepath = r"C:\Arbeitplatz\03_ImageJ_script_learning\pegaij"
modulename = r"pegaij"
sys.path.append(modulepath)

ScriptPath = modulepath + modulename + "$py.class"
if isfile(ScriptPath):
	os.remove(ScriptPath)

print(sys.path)
import pegaij as pi

print(pi.sum(2,3))