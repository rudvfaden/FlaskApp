
import math


def chairAngles(rake, splay):
	if rake>0 and splay>0:
	    r_rake = math.radians(rake)
	    r_splay = math.radians(splay)
	    t_rake = math.tan(r_rake)
	    t_splay = math.tan(r_splay)
	    sigthAngle = math.atan(t_rake/t_splay)
	    resultant = math.atan(t_rake/math.sin(sigthAngle))
	    return math.degrees(sigthAngle), math.degrees(resultant)
	else:
		return -1,-1

sigthAngle, resultant = chairAngles(15, 22)
