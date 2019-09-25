from ij import IJ, ImagePlus

# Grap the last activated image
imp = IJ.getImage()

# Print image details
print("title: ", imp.title)
print("width: ", imp.width)
print("height: ", imp.height)
print("number of pixels: ", imp.width * imp.height)
print("number of slices: ", imp.getNSlices())
print("number of channels: ", imp.getNChannels())
print("number of time frames: ", imp.getNFrames())

types = {ImagePlus.COLOR_RGB : "RGB",
		 ImagePlus.GRAY8 : "8-bit",
		 ImagePlus.GRAY16 : "16-bit", 
		 ImagePlus.GRAY32 : "32-bit",
		 ImagePlus.COLOR_256 : "8-bit color"
		 }

print("image type: ", types[imp.type])
		 