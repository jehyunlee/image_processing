from ij import IJ

imp = IJ.getImage()

# Macro에서 읽어온 명령어를 Ctrl+C/V
IJ.run(imp, "Median...", "radius=2")
