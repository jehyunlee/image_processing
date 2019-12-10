from javax.swing import JFrame, JButton, JOptionPane
from ij import IJ, WindowManager as WM

def measure(event):
    """ event: the ActionEvent that tells us about the button having been clicked. """ 
    imp = WM.getCurrentImage()
    print imp
    if imp:
        IJ.run(imp, "Measure", "")
    else:
        print "Open an image first."

frame = JFrame("Measure", visible=True)
button = JButton("Area", actionPerformed=measure)
frame.getContentPane().add(button)
frame.pack()
