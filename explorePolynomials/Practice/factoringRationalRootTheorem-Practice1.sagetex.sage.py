## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file factoringRationalRootTheorem-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_89 = Integer(89); _sage_const_5 = Integer(5); _sage_const_67 = Integer(67); _sage_const_100 = Integer(100); _sage_const_43 = Integer(43); _sage_const_9 = Integer(9); _sage_const_4 = Integer(4); _sage_const_78 = Integer(78); _sage_const_95 = Integer(95); _sage_const_10 = Integer(10); _sage_const_6 = Integer(6)## This file (factoringRationalRootTheorem-Practice1.sagetex.sage) was *autogenerated* from factoringRationalRootTheorem-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('factoringRationalRootTheorem-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_1 
_st_.blockbegin()
try:
 
 ######  Define a function to convert a sage number into a saved counter number.
 
 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(_sage_const_0 )
 
 def DispSign(b):
     """ Returns the string of the 'signed' version of `b`, e.g. 3 -> "+3", -3 -> "-3", 0 -> "".
     """
     if b == _sage_const_0 :
         return ""
     elif b > _sage_const_0 :
         return "+" + str(b)
     elif b < _sage_const_0 :
         return str(b)
     else:
         # If we're here, then something has gone wrong.
         raise ValueError
 
 def ISP(b):
     return DispSign(b)
 
 def NoEval(f, c):
     # TODO
     """ Returns a non-evaluted version of the result f(c).
     """
     cStr = str(c)
     # fLatex = latex(f)
     fString = latex(f)
     fStrList = list(fString)
     length = len(fStrList)
     fStrList2 = range(length)
     for i in range(_sage_const_0 , length):
         if fStrList[i] == "x":
             fStrList2[i] = "("+cstr+")"
         else:
             fStrList2[i] = fStrList[i]
     f2 = join(fStrList2,"")
     return LatexExpr(f2)
 
 def HyperSimp(f):
     """ Returns the expression `f` without hyperbolic expressions.
     """
     subsDict = {
         sinh(w0) : (exp(w0) - exp(-w0))/_sage_const_2 ,
         cosh(w0) : (exp(w0) + exp(-w0))/_sage_const_2 ,
         tanh(w0) : (exp(w0) - exp(-w0))/(exp(w0) + exp(-w0)),
         sech(w0) : _sage_const_2 /(exp(w0) + exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         csch(w0) : _sage_const_2 /(exp(w0) - exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         coth(w0) : (exp(w0) + exp(-w0))/(exp(w0) - exp(-w0)),   # This seems to work, but Nowell said it didn't at one point.
         arcsinh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  + _sage_const_1 ) ),
         arccosh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  - _sage_const_1 ) ),
         arctanh(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (_sage_const_1  - w0) ),
         arccsch(w0) :       ln( (_sage_const_1  + sqrt((w0)**_sage_const_2  + _sage_const_1 ))/w0 ),
         arcsech(w0) :       ln( (_sage_const_1  + sqrt(_sage_const_1  - (w0)**_sage_const_2 ))/w0 ),
         arccoth(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (w0 - _sage_const_1 ) )
     }
     g = f.substitute(subsDict)
     return simplify(g)
 
 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))
 
 def NonZeroInt(b,c, avoid = [_sage_const_0 ]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a
 
 def RandVector(b, c, avoid=[], rep=_sage_const_1 ):
     """ Returns essentially a multiset permutation of ([b,c]-av) * rep.
         That is, a vector which contains each integer in [`b`,`c`] which is not in `av` a total of `rep` number of times.
         Example:
         sage: RandVector(1,3, [2], 2)
         [3, 1, 1, 3]
     """
     oneVec = [val for val in range(b,c+_sage_const_1 ) if val not in avoid]
     vec = oneVec * rep
     shuffle(vec)
     return vec
 
 
except:
 _st_.goboom(_sage_const_95 )
_st_.blockend()
_st_.current_tex_line = _sage_const_9 
_st_.blockbegin()
try:
 ###### Problem p1
 p1c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c3 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1f1 = expand((x-p1c1)*(x-p1c2)*(x-p1c3)*(x-p1c4))
 
 
 ###### Problem p2
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c3 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2f1 = expand((x-p2c1)*(x-p2c2)*(x-p2c3)*(x-p2c4))
 
 
 ###### Problem p3
 p3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c3 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3f1 = expand((x-p3c1)*(x-p3c2)*(x-p3c3)*(x-p3c4))
 
 
 ###### Problem p4
 p4c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4c3 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4f1 = expand((x-p4c1)*(x-p4c2)*(x-p4c3)*(x-p4c4))
 
 
 
except:
 _st_.goboom(_sage_const_43 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_0 , latex(p1f1))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_67 
 _st_.inline(_sage_const_1 , latex(p1f1))
except:
 _st_.goboom(_sage_const_67 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_2 , latex(p2f1))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_3 , latex(p2f1))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_4 , latex(p3f1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_5 , latex(p3f1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_6 , latex(p4f1))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_7 , latex(p4f1))
except:
 _st_.goboom(_sage_const_100 )
_st_.endofdoc()
