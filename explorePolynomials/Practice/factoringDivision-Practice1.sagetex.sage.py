## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file factoringDivision-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_63 = Integer(63); _sage_const_113 = Integer(113); _sage_const_86 = Integer(86); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_104 = Integer(104); _sage_const_95 = Integer(95)## This file (factoringDivision-Practice1.sagetex.sage) was *autogenerated* from factoringDivision-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('factoringDivision-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
 p1pwr1 = RandInt(_sage_const_1 ,_sage_const_2 )
 p1pwr2 = RandInt(_sage_const_2 ,_sage_const_5 )
 p1f0 = sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p1pwr1-_sage_const_1 ))])
 
 
 p1f1 = p1c1*x**p1pwr1 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p1pwr1-_sage_const_1 ))])
 p1f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*x**p1pwr2 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p1pwr2-_sage_const_1 ))])
 p1f3 = expand(p1f1*p1f2) + p1f0
 
 
 ###### Problem p2
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2pwr1 = RandInt(_sage_const_1 ,_sage_const_2 )
 p2pwr2 = RandInt(_sage_const_2 ,_sage_const_5 )
 p2f0 = sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p2pwr1-_sage_const_1 ))])
 
 
 p2f1 = p2c1*x**p2pwr1 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p2pwr1-_sage_const_1 ))])
 p2f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*x**p2pwr2 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p2pwr2-_sage_const_1 ))])
 p2f3 = expand(p2f1*p2f2) + p2f0
 
 
 ###### Problem p3
 p3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3pwr1 = RandInt(_sage_const_1 ,_sage_const_2 )
 p3pwr2 = RandInt(_sage_const_2 ,_sage_const_5 )
 p3f0 = sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p3pwr1-_sage_const_1 ))])
 
 
 p3f1 = p3c1*x**p3pwr1 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p3pwr1-_sage_const_1 ))])
 p3f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*x**p3pwr2 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p3pwr2-_sage_const_1 ))])
 p3f3 = expand(p3f1*p3f2) + p3f0
 
 
 ###### Problem p4
 p4c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4pwr1 = RandInt(_sage_const_1 ,_sage_const_2 )
 p4pwr2 = RandInt(_sage_const_2 ,_sage_const_5 )
 p4f0 = sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p4pwr1-_sage_const_1 ))])
 
 
 p4f1 = p4c1*x**p4pwr1 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p4pwr1-_sage_const_1 ))])
 p4f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*x**p4pwr2 + sum([RandInt(-_sage_const_5 ,_sage_const_5 )*x**t for t in (ellipsis_range(_sage_const_0 ,Ellipsis,p4pwr2-_sage_const_1 ))])
 p4f3 = expand(p4f1*p4f2) + p4f0
 
 
 
except:
 _st_.goboom(_sage_const_63 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_0 , latex(p1f3))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_1 , latex(p1f1))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_2 , latex(p1f2))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_3 , latex(p1f0))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_4 , latex(p1f1))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_5 , latex(p2f3))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_6 , latex(p2f1))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_7 , latex(p2f2))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_8 , latex(p2f0))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_9 , latex(p2f1))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_10 , latex(p3f3))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_11 , latex(p3f1))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_12 , latex(p3f2))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_13 , latex(p3f0))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_14 , latex(p3f1))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_15 , latex(p4f3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_16 , latex(p4f1))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_17 , latex(p4f2))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_18 , latex(p4f0))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_19 , latex(p4f1))
except:
 _st_.goboom(_sage_const_113 )
_st_.endofdoc()

