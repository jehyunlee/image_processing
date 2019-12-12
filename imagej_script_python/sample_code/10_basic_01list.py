from java.awt.geom import AffineTransform
from array import array

# 2D point
x = 10
y = 40

# Affine transformation
# https://docs.oracle.com/javase/1.5.0/docs/api/java/awt/geom/AffineTransform.html
# https://darkpgmr.tistory.com/79
# [ x']   [  m00  m01  m02  ] [ x ]   [ m00x + m01y + m02 ]
# [ y'] = [  m10  m11  m12  ] [ y ] = [ m10x + m11y + m12 ]
# [ 1 ]   [   0    0    1   ] [ 1 ]   [         1         ]
# AffineTransform(float m00, float m10, float m01, float m11, float m02, float m12)
aff = AffineTransform(1, 0, 0, 1, 45, 56)

# Create a point as a list of x, y
p = [x, y]
# transform(float[] srcPts, int srcOff, float[] dstPts, int dstOff, int numPts)
aff.transform(p, 0, p, 0, 1)
print "p=", p # 그대로 [10, 40]. update 안됨.LookupError

# Create a point as a native float array of x, y
q = array('f', [x, y])
aff.transform(q, 0, q, 0, 1)
print "q=", q
