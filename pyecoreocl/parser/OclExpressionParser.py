# Generated from OclExpression.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


OBJ = object
CANNOT_EVAL = object()  # define a sentinel object

def has_result(*args):
    return all(e.r is not None and e.r is not CANNOT_EVAL for e in args)

def f(vs, ts, eval):
    for v, t in zip(vs, ts):
        if v is CANNOT_EVAL or not isinstance(v, t):
            return CANNOT_EVAL
    return eval(*vs)

def serializedATN():
    return [
        4,1,61,437,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,4,0,71,8,0,11,0,12,0,72,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,86,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,175,8,0,10,0,
        12,0,178,9,0,1,1,1,1,1,1,1,1,5,1,184,8,1,10,1,12,1,187,9,1,3,1,189,
        8,1,1,1,1,1,1,1,1,1,1,1,5,1,196,8,1,10,1,12,1,199,9,1,1,1,1,1,3,
        1,203,8,1,1,1,1,1,1,1,1,1,3,1,209,8,1,1,1,1,1,1,1,3,1,214,8,1,1,
        1,1,1,1,1,1,1,3,1,220,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,234,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,261,
        8,5,1,6,1,6,1,6,1,6,1,6,5,6,268,8,6,10,6,12,6,271,9,6,1,6,1,6,1,
        7,1,7,1,7,3,7,278,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,288,8,
        8,10,8,12,8,291,9,8,3,8,293,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,306,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,318,8,10,1,11,1,11,1,11,1,11,1,11,3,11,325,8,11,1,
        12,1,12,1,12,1,12,1,12,3,12,332,8,12,1,13,1,13,1,14,1,14,1,14,1,
        14,5,14,340,8,14,10,14,12,14,343,9,14,1,14,1,14,1,14,1,15,1,15,1,
        15,3,15,351,8,15,1,15,1,15,1,15,1,16,1,16,3,16,358,8,16,1,17,1,17,
        1,17,1,17,1,17,1,17,4,17,366,8,17,11,17,12,17,367,5,17,370,8,17,
        10,17,12,17,373,9,17,1,18,1,18,1,18,3,18,378,8,18,1,19,1,19,1,19,
        1,19,1,19,5,19,385,8,19,10,19,12,19,388,9,19,1,19,1,19,1,19,1,19,
        1,19,1,19,5,19,396,8,19,10,19,12,19,399,9,19,1,19,1,19,3,19,403,
        8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,3,22,421,8,22,1,23,1,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,0,2,0,34,30,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,0,3,1,0,51,52,6,0,5,5,15,19,21,21,25,26,29,43,45,55,
        5,0,5,5,15,19,21,21,25,25,45,54,480,0,85,1,0,0,0,2,219,1,0,0,0,4,
        233,1,0,0,0,6,235,1,0,0,0,8,237,1,0,0,0,10,260,1,0,0,0,12,262,1,
        0,0,0,14,274,1,0,0,0,16,282,1,0,0,0,18,296,1,0,0,0,20,317,1,0,0,
        0,22,324,1,0,0,0,24,331,1,0,0,0,26,333,1,0,0,0,28,335,1,0,0,0,30,
        347,1,0,0,0,32,357,1,0,0,0,34,359,1,0,0,0,36,377,1,0,0,0,38,379,
        1,0,0,0,40,404,1,0,0,0,42,408,1,0,0,0,44,420,1,0,0,0,46,422,1,0,
        0,0,48,424,1,0,0,0,50,426,1,0,0,0,52,428,1,0,0,0,54,430,1,0,0,0,
        56,432,1,0,0,0,58,434,1,0,0,0,60,61,6,0,-1,0,61,62,3,4,2,0,62,63,
        6,0,-1,0,63,86,1,0,0,0,64,65,3,56,28,0,65,66,6,0,-1,0,66,86,1,0,
        0,0,67,68,3,56,28,0,68,69,5,1,0,0,69,71,1,0,0,0,70,67,1,0,0,0,71,
        72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,3,58,
        29,0,75,76,6,0,-1,0,76,86,1,0,0,0,77,78,5,4,0,0,78,79,3,0,0,16,79,
        80,6,0,-1,0,80,86,1,0,0,0,81,82,5,5,0,0,82,83,3,0,0,15,83,84,6,0,
        -1,0,84,86,1,0,0,0,85,60,1,0,0,0,85,64,1,0,0,0,85,70,1,0,0,0,85,
        77,1,0,0,0,85,81,1,0,0,0,86,176,1,0,0,0,87,88,10,14,0,0,88,89,5,
        6,0,0,89,90,3,0,0,15,90,91,6,0,-1,0,91,175,1,0,0,0,92,93,10,13,0,
        0,93,94,5,7,0,0,94,95,3,0,0,14,95,96,6,0,-1,0,96,175,1,0,0,0,97,
        98,10,12,0,0,98,99,5,8,0,0,99,100,3,0,0,13,100,101,6,0,-1,0,101,
        175,1,0,0,0,102,103,10,11,0,0,103,104,5,4,0,0,104,105,3,0,0,12,105,
        106,6,0,-1,0,106,175,1,0,0,0,107,108,10,10,0,0,108,109,5,9,0,0,109,
        110,3,0,0,11,110,111,6,0,-1,0,111,175,1,0,0,0,112,113,10,9,0,0,113,
        114,5,10,0,0,114,115,3,0,0,10,115,116,6,0,-1,0,116,175,1,0,0,0,117,
        118,10,8,0,0,118,119,5,11,0,0,119,120,3,0,0,9,120,121,6,0,-1,0,121,
        175,1,0,0,0,122,123,10,7,0,0,123,124,5,12,0,0,124,125,3,0,0,8,125,
        126,6,0,-1,0,126,175,1,0,0,0,127,128,10,6,0,0,128,129,5,13,0,0,129,
        130,3,0,0,7,130,131,6,0,-1,0,131,175,1,0,0,0,132,133,10,5,0,0,133,
        134,5,14,0,0,134,135,3,0,0,6,135,136,6,0,-1,0,136,175,1,0,0,0,137,
        138,10,4,0,0,138,139,5,15,0,0,139,140,3,0,0,5,140,141,6,0,-1,0,141,
        175,1,0,0,0,142,143,10,3,0,0,143,144,5,16,0,0,144,145,3,0,0,4,145,
        146,6,0,-1,0,146,175,1,0,0,0,147,148,10,2,0,0,148,149,5,17,0,0,149,
        175,3,0,0,3,150,151,10,1,0,0,151,152,5,18,0,0,152,175,3,0,0,2,153,
        154,10,20,0,0,154,155,3,2,1,0,155,156,6,0,-1,0,156,175,1,0,0,0,157,
        158,10,19,0,0,158,159,5,2,0,0,159,160,3,56,28,0,160,161,3,2,1,0,
        161,162,6,0,-1,0,162,175,1,0,0,0,163,164,10,18,0,0,164,165,5,2,0,
        0,165,166,3,56,28,0,166,167,6,0,-1,0,167,175,1,0,0,0,168,169,10,
        17,0,0,169,170,5,3,0,0,170,171,3,56,28,0,171,172,3,2,1,0,172,173,
        6,0,-1,0,173,175,1,0,0,0,174,87,1,0,0,0,174,92,1,0,0,0,174,97,1,
        0,0,0,174,102,1,0,0,0,174,107,1,0,0,0,174,112,1,0,0,0,174,117,1,
        0,0,0,174,122,1,0,0,0,174,127,1,0,0,0,174,132,1,0,0,0,174,137,1,
        0,0,0,174,142,1,0,0,0,174,147,1,0,0,0,174,150,1,0,0,0,174,153,1,
        0,0,0,174,157,1,0,0,0,174,163,1,0,0,0,174,168,1,0,0,0,175,178,1,
        0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,1,1,0,0,0,178,176,1,0,
        0,0,179,188,5,19,0,0,180,185,3,0,0,0,181,182,5,20,0,0,182,184,3,
        0,0,0,183,181,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,
        0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,188,180,1,0,0,0,188,189,1,
        0,0,0,189,190,1,0,0,0,190,220,5,21,0,0,191,192,5,19,0,0,192,197,
        3,58,29,0,193,194,5,20,0,0,194,196,3,58,29,0,195,193,1,0,0,0,196,
        199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,202,1,0,0,0,199,
        197,1,0,0,0,200,201,5,22,0,0,201,203,3,32,16,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,213,1,0,0,0,204,205,5,23,0,0,205,208,3,58,29,0,206,
        207,5,22,0,0,207,209,3,32,16,0,208,206,1,0,0,0,208,209,1,0,0,0,209,
        210,1,0,0,0,210,211,5,13,0,0,211,212,3,0,0,0,212,214,1,0,0,0,213,
        204,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,216,5,24,0,0,216,
        217,3,0,0,0,217,218,5,21,0,0,218,220,1,0,0,0,219,179,1,0,0,0,219,
        191,1,0,0,0,220,3,1,0,0,0,221,234,3,6,3,0,222,223,3,8,4,0,223,224,
        6,2,-1,0,224,234,1,0,0,0,225,226,3,10,5,0,226,227,6,2,-1,0,227,234,
        1,0,0,0,228,234,3,12,6,0,229,234,3,16,8,0,230,234,3,26,13,0,231,
        234,3,28,14,0,232,234,3,42,21,0,233,221,1,0,0,0,233,222,1,0,0,0,
        233,225,1,0,0,0,233,228,1,0,0,0,233,229,1,0,0,0,233,230,1,0,0,0,
        233,231,1,0,0,0,233,232,1,0,0,0,234,5,1,0,0,0,235,236,5,25,0,0,236,
        7,1,0,0,0,237,238,5,19,0,0,238,239,3,0,0,0,239,240,5,21,0,0,240,
        241,6,4,-1,0,241,9,1,0,0,0,242,243,3,44,22,0,243,244,6,5,-1,0,244,
        261,1,0,0,0,245,246,3,48,24,0,246,247,6,5,-1,0,247,261,1,0,0,0,248,
        249,3,46,23,0,249,250,6,5,-1,0,250,261,1,0,0,0,251,252,3,50,25,0,
        252,253,6,5,-1,0,253,261,1,0,0,0,254,255,3,52,26,0,255,256,6,5,-1,
        0,256,261,1,0,0,0,257,258,3,54,27,0,258,259,6,5,-1,0,259,261,1,0,
        0,0,260,242,1,0,0,0,260,245,1,0,0,0,260,248,1,0,0,0,260,251,1,0,
        0,0,260,254,1,0,0,0,260,257,1,0,0,0,261,11,1,0,0,0,262,263,5,26,
        0,0,263,264,5,27,0,0,264,269,3,14,7,0,265,266,5,20,0,0,266,268,3,
        14,7,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,1,
        0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,5,28,0,0,273,13,1,
        0,0,0,274,277,3,56,28,0,275,276,5,22,0,0,276,278,3,32,16,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,5,13,0,0,280,281,
        3,4,2,0,281,15,1,0,0,0,282,283,3,18,9,0,283,292,5,27,0,0,284,289,
        3,24,12,0,285,286,5,20,0,0,286,288,3,24,12,0,287,285,1,0,0,0,288,
        291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,293,1,0,0,0,291,
        289,1,0,0,0,292,284,1,0,0,0,292,293,1,0,0,0,293,294,1,0,0,0,294,
        295,5,28,0,0,295,17,1,0,0,0,296,305,3,22,11,0,297,298,5,19,0,0,298,
        299,3,32,16,0,299,300,5,21,0,0,300,306,1,0,0,0,301,302,5,9,0,0,302,
        303,3,32,16,0,303,304,5,10,0,0,304,306,1,0,0,0,305,297,1,0,0,0,305,
        301,1,0,0,0,305,306,1,0,0,0,306,19,1,0,0,0,307,318,5,29,0,0,308,
        318,5,30,0,0,309,318,5,31,0,0,310,318,5,32,0,0,311,318,5,33,0,0,
        312,318,5,34,0,0,313,318,5,35,0,0,314,318,5,36,0,0,315,318,5,37,
        0,0,316,318,5,38,0,0,317,307,1,0,0,0,317,308,1,0,0,0,317,309,1,0,
        0,0,317,310,1,0,0,0,317,311,1,0,0,0,317,312,1,0,0,0,317,313,1,0,
        0,0,317,314,1,0,0,0,317,315,1,0,0,0,317,316,1,0,0,0,318,21,1,0,0,
        0,319,325,5,39,0,0,320,325,5,40,0,0,321,325,5,41,0,0,322,325,5,42,
        0,0,323,325,5,43,0,0,324,319,1,0,0,0,324,320,1,0,0,0,324,321,1,0,
        0,0,324,322,1,0,0,0,324,323,1,0,0,0,325,23,1,0,0,0,326,332,3,0,0,
        0,327,328,3,0,0,0,328,329,5,44,0,0,329,330,3,0,0,0,330,332,1,0,0,
        0,331,326,1,0,0,0,331,327,1,0,0,0,332,25,1,0,0,0,333,334,3,36,18,
        0,334,27,1,0,0,0,335,336,5,45,0,0,336,341,3,30,15,0,337,338,5,20,
        0,0,338,340,3,30,15,0,339,337,1,0,0,0,340,343,1,0,0,0,341,339,1,
        0,0,0,341,342,1,0,0,0,342,344,1,0,0,0,343,341,1,0,0,0,344,345,5,
        46,0,0,345,346,3,0,0,0,346,29,1,0,0,0,347,350,3,56,28,0,348,349,
        5,22,0,0,349,351,3,32,16,0,350,348,1,0,0,0,350,351,1,0,0,0,351,352,
        1,0,0,0,352,353,5,13,0,0,353,354,3,0,0,0,354,31,1,0,0,0,355,358,
        3,36,18,0,356,358,3,34,17,0,357,355,1,0,0,0,357,356,1,0,0,0,358,
        33,1,0,0,0,359,360,6,17,-1,0,360,361,3,56,28,0,361,371,1,0,0,0,362,
        365,10,1,0,0,363,364,5,1,0,0,364,366,3,58,29,0,365,363,1,0,0,0,366,
        367,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,
        362,1,0,0,0,370,373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,
        35,1,0,0,0,373,371,1,0,0,0,374,378,3,18,9,0,375,378,3,20,10,0,376,
        378,3,38,19,0,377,374,1,0,0,0,377,375,1,0,0,0,377,376,1,0,0,0,378,
        37,1,0,0,0,379,402,5,26,0,0,380,381,5,19,0,0,381,386,3,40,20,0,382,
        383,5,20,0,0,383,385,3,40,20,0,384,382,1,0,0,0,385,388,1,0,0,0,386,
        384,1,0,0,0,386,387,1,0,0,0,387,389,1,0,0,0,388,386,1,0,0,0,389,
        390,5,21,0,0,390,403,1,0,0,0,391,392,5,9,0,0,392,397,3,40,20,0,393,
        394,5,20,0,0,394,396,3,40,20,0,395,393,1,0,0,0,396,399,1,0,0,0,397,
        395,1,0,0,0,397,398,1,0,0,0,398,400,1,0,0,0,399,397,1,0,0,0,400,
        401,5,10,0,0,401,403,1,0,0,0,402,380,1,0,0,0,402,391,1,0,0,0,402,
        403,1,0,0,0,403,39,1,0,0,0,404,405,3,56,28,0,405,406,5,22,0,0,406,
        407,3,32,16,0,407,41,1,0,0,0,408,409,5,47,0,0,409,410,3,0,0,0,410,
        411,5,48,0,0,411,412,3,0,0,0,412,413,5,49,0,0,413,414,3,0,0,0,414,
        415,5,50,0,0,415,43,1,0,0,0,416,417,5,59,0,0,417,421,6,22,-1,0,418,
        419,5,60,0,0,419,421,6,22,-1,0,420,416,1,0,0,0,420,418,1,0,0,0,421,
        45,1,0,0,0,422,423,5,56,0,0,423,47,1,0,0,0,424,425,7,0,0,0,425,49,
        1,0,0,0,426,427,5,6,0,0,427,51,1,0,0,0,428,429,5,53,0,0,429,53,1,
        0,0,0,430,431,5,54,0,0,431,55,1,0,0,0,432,433,8,1,0,0,433,57,1,0,
        0,0,434,435,8,2,0,0,435,59,1,0,0,0,31,72,85,174,176,185,188,197,
        202,208,213,219,233,260,269,277,289,292,305,317,324,331,341,350,
        357,367,371,377,386,397,402,420
    ]

class OclExpressionParser ( Parser ):

    grammarFileName = "OclExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'.'", "'->'", "'-'", "'not'", 
                     "'*'", "'/'", "'+'", "'<'", "'>'", "'<='", "'>='", 
                     "'='", "'<>'", "'and'", "'or'", "'xor'", "'implies'", 
                     "'('", "','", "')'", "':'", "';'", "'|'", "'self'", 
                     "'Tuple'", "'{'", "'}'", "'String'", "'Integer'", "'UnlimitedNatural'", 
                     "'Boolean'", "'Real'", "'OclAny'", "'OclInvalid'", 
                     "'OclMessage'", "'OclSelf'", "'OclVoid'", "'Collection'", 
                     "'Bag'", "'OrderedSet'", "'Sequence'", "'Set'", "'..'", 
                     "'let'", "'in'", "'if'", "'then'", "'else'", "'endif'", 
                     "'true'", "'false'", "'invalid'", "'null'", "'Lambda'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "SPECIAL_VARNAME", "VARNAME", "INT", "FLOAT", 
                      "WS" ]

    RULE_oclExp = 0
    RULE_argExp = 1
    RULE_primaryExp = 2
    RULE_selfExp = 3
    RULE_nestedExp = 4
    RULE_primitiveLiteralExp = 5
    RULE_tupleLiteralExp = 6
    RULE_tupleLiteralPartCS = 7
    RULE_collectionLiteralExp = 8
    RULE_collectionTypeCS = 9
    RULE_primitiveTypeCS = 10
    RULE_collectionTypeIdentifier = 11
    RULE_collectionLiteralPartCS = 12
    RULE_typeLiteralExp = 13
    RULE_letExp = 14
    RULE_letVariableCS = 15
    RULE_typeExpCS = 16
    RULE_typeNameExpCS = 17
    RULE_typeLiteralCS = 18
    RULE_tupleTypeCS = 19
    RULE_tuplePartCS = 20
    RULE_ifExp = 21
    RULE_numberLiteralExpCS = 22
    RULE_stringLiteralExpCS = 23
    RULE_booleanLiteralExpCS = 24
    RULE_unlimitedNaturalLiteralCS = 25
    RULE_invalidLiteralExpCS = 26
    RULE_nullLiteralExpCS = 27
    RULE_unrestrictedName = 28
    RULE_unreservedName = 29

    ruleNames =  [ "oclExp", "argExp", "primaryExp", "selfExp", "nestedExp", 
                   "primitiveLiteralExp", "tupleLiteralExp", "tupleLiteralPartCS", 
                   "collectionLiteralExp", "collectionTypeCS", "primitiveTypeCS", 
                   "collectionTypeIdentifier", "collectionLiteralPartCS", 
                   "typeLiteralExp", "letExp", "letVariableCS", "typeExpCS", 
                   "typeNameExpCS", "typeLiteralCS", "tupleTypeCS", "tuplePartCS", 
                   "ifExp", "numberLiteralExpCS", "stringLiteralExpCS", 
                   "booleanLiteralExpCS", "unlimitedNaturalLiteralCS", "invalidLiteralExpCS", 
                   "nullLiteralExpCS", "unrestrictedName", "unreservedName" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    STRING=56
    SPECIAL_VARNAME=57
    VARNAME=58
    INT=59
    FLOAT=60
    WS=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OclExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None


        def getRuleIndex(self):
            return OclExpressionParser.RULE_oclExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.r = ctx.r


    class UnaryOperationContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.operator = None # Token
            self.expression = None # OclExpContext
            self.copyFrom(ctx)

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperation" ):
                listener.enterUnaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperation" ):
                listener.exitUnaryOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperation" ):
                return visitor.visitUnaryOperation(self)
            else:
                return visitor.visitChildren(self)


    class AttributeNavigationContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.expression = None # OclExpContext
            self.attname = None # UnrestrictedNameContext
            self.copyFrom(ctx)

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeNavigation" ):
                listener.enterAttributeNavigation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeNavigation" ):
                listener.exitAttributeNavigation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeNavigation" ):
                return visitor.visitAttributeNavigation(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExpressionContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.n = None # PrimaryExpContext
            self.copyFrom(ctx)

        def primaryExp(self):
            return self.getTypedRuleContext(OclExpressionParser.PrimaryExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticBinaryOperationContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.left = None # OclExpContext
            self.operator = None # Token
            self.right = None # OclExpContext
            self.copyFrom(ctx)

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticBinaryOperation" ):
                listener.enterArithmeticBinaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticBinaryOperation" ):
                listener.exitArithmeticBinaryOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticBinaryOperation" ):
                return visitor.visitArithmeticBinaryOperation(self)
            else:
                return visitor.visitChildren(self)


    class SimpleNameContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleName" ):
                listener.enterSimpleName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleName" ):
                listener.exitSimpleName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleName" ):
                return visitor.visitSimpleName(self)
            else:
                return visitor.visitChildren(self)


    class FullQualifiedNameContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unreservedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnreservedNameContext,0)

        def unrestrictedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.UnrestrictedNameContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullQualifiedName" ):
                listener.enterFullQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullQualifiedName" ):
                listener.exitFullQualifiedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullQualifiedName" ):
                return visitor.visitFullQualifiedName(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonBinaryOperationContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.left = None # OclExpContext
            self.operator = None # Token
            self.right = None # OclExpContext
            self.copyFrom(ctx)

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonBinaryOperation" ):
                listener.enterComparisonBinaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonBinaryOperation" ):
                listener.exitComparisonBinaryOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonBinaryOperation" ):
                return visitor.visitComparisonBinaryOperation(self)
            else:
                return visitor.visitChildren(self)


    class CollectionCallContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.expression = None # OclExpContext
            self.attname = None # UnrestrictedNameContext
            self.copyFrom(ctx)

        def argExp(self):
            return self.getTypedRuleContext(OclExpressionParser.ArgExpContext,0)

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionCall" ):
                listener.enterCollectionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionCall" ):
                listener.exitCollectionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionCall" ):
                return visitor.visitCollectionCall(self)
            else:
                return visitor.visitChildren(self)


    class BooleanBinaryOperationContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.left = None # OclExpContext
            self.operator = None # Token
            self.right = None # OclExpContext
            self.copyFrom(ctx)

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanBinaryOperation" ):
                listener.enterBooleanBinaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanBinaryOperation" ):
                listener.exitBooleanBinaryOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanBinaryOperation" ):
                return visitor.visitBooleanBinaryOperation(self)
            else:
                return visitor.visitChildren(self)


    class CallExpressionContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.expression = None # OclExpContext
            self.copyFrom(ctx)

        def argExp(self):
            return self.getTypedRuleContext(OclExpressionParser.ArgExpContext,0)

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpression" ):
                listener.enterCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpression" ):
                listener.exitCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpression" ):
                return visitor.visitCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallContext(OclExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.OclExpContext
            super().__init__(parser)
            self.expression = None # OclExpContext
            self.attname = None # UnrestrictedNameContext
            self.copyFrom(ctx)

        def argExp(self):
            return self.getTypedRuleContext(OclExpressionParser.ArgExpContext,0)

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)



    def oclExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OclExpressionParser.OclExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_oclExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = OclExpressionParser.PrimaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 61
                localctx.n = self.primaryExp()
                localctx.r = localctx.n.r
                pass

            elif la_ == 2:
                localctx = OclExpressionParser.SimpleNameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.unrestrictedName()
                localctx.r = CANNOT_EVAL
                pass

            elif la_ == 3:
                localctx = OclExpressionParser.FullQualifiedNameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 67
                        self.unrestrictedName()
                        self.state = 68
                        self.match(OclExpressionParser.T__0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 72 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 74
                self.unreservedName()
                localctx.r = CANNOT_EVAL
                pass

            elif la_ == 4:
                localctx = OclExpressionParser.UnaryOperationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                localctx.operator = self.match(OclExpressionParser.T__3)
                self.state = 78
                localctx.expression = self.oclExp(16)
                localctx.r = f((localctx.expression.r,), ((int, float),), lambda n: -n)
                pass

            elif la_ == 5:
                localctx = OclExpressionParser.UnaryOperationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                localctx.operator = self.match(OclExpressionParser.T__4)
                self.state = 82
                localctx.expression = self.oclExp(15)
                localctx.r = f((localctx.expression.r,), (bool,), lambda n: not n)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = OclExpressionParser.ArithmeticBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 87
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 88
                        localctx.operator = self.match(OclExpressionParser.T__5)
                        self.state = 89
                        localctx.right = self.oclExp(15)
                        localctx.r = f((localctx.left.r, localctx.right.r), (int, int), lambda l, r: l * r)
                        pass

                    elif la_ == 2:
                        localctx = OclExpressionParser.ArithmeticBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 92
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 93
                        localctx.operator = self.match(OclExpressionParser.T__6)
                        self.state = 94
                        localctx.right = self.oclExp(14)
                        localctx.r = f((localctx.left.r, localctx.right.r), (int, int), lambda l, r: l / r)
                        pass

                    elif la_ == 3:
                        localctx = OclExpressionParser.ArithmeticBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 97
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 98
                        localctx.operator = self.match(OclExpressionParser.T__7)
                        self.state = 99
                        localctx.right = self.oclExp(13)
                        localctx.r = f((localctx.left.r, localctx.right.r), (int, int), lambda l, r: l + r)
                        pass

                    elif la_ == 4:
                        localctx = OclExpressionParser.ArithmeticBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 102
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 103
                        localctx.operator = self.match(OclExpressionParser.T__3)
                        self.state = 104
                        localctx.right = self.oclExp(12)
                        localctx.r = f((localctx.left.r, localctx.right.r), (int, int), lambda l, r: l - r)
                        pass

                    elif la_ == 5:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 107
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 108
                        localctx.operator = self.match(OclExpressionParser.T__8)
                        self.state = 109
                        localctx.right = self.oclExp(11)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l < r)
                        pass

                    elif la_ == 6:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 112
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 113
                        localctx.operator = self.match(OclExpressionParser.T__9)
                        self.state = 114
                        localctx.right = self.oclExp(10)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l > r)
                        pass

                    elif la_ == 7:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 117
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 118
                        localctx.operator = self.match(OclExpressionParser.T__10)
                        self.state = 119
                        localctx.right = self.oclExp(9)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l <= r)
                        pass

                    elif la_ == 8:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 122
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 123
                        localctx.operator = self.match(OclExpressionParser.T__11)
                        self.state = 124
                        localctx.right = self.oclExp(8)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l >= r)
                        pass

                    elif la_ == 9:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 127
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 128
                        localctx.operator = self.match(OclExpressionParser.T__12)
                        self.state = 129
                        localctx.right = self.oclExp(7)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l == r)
                        pass

                    elif la_ == 10:
                        localctx = OclExpressionParser.ComparisonBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 133
                        localctx.operator = self.match(OclExpressionParser.T__13)
                        self.state = 134
                        localctx.right = self.oclExp(6)
                        localctx.r = f((localctx.left.r, localctx.right.r), (OBJ, OBJ), lambda l, r: l != r)
                        pass

                    elif la_ == 11:
                        localctx = OclExpressionParser.BooleanBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 137
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 138
                        localctx.operator = self.match(OclExpressionParser.T__14)
                        self.state = 139
                        localctx.right = self.oclExp(5)
                        localctx.r = f((localctx.left.r, localctx.right.r), (bool, bool), lambda l, r: l and r)
                        pass

                    elif la_ == 12:
                        localctx = OclExpressionParser.BooleanBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 142
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 143
                        localctx.operator = self.match(OclExpressionParser.T__15)
                        self.state = 144
                        localctx.right = self.oclExp(4)
                        localctx.r = f((localctx.left.r, localctx.right.r), (bool, bool), lambda l, r: l or r)
                        pass

                    elif la_ == 13:
                        localctx = OclExpressionParser.BooleanBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 147
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 148
                        localctx.operator = self.match(OclExpressionParser.T__16)
                        self.state = 149
                        localctx.right = self.oclExp(3)
                        pass

                    elif la_ == 14:
                        localctx = OclExpressionParser.BooleanBinaryOperationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 150
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 151
                        localctx.operator = self.match(OclExpressionParser.T__17)
                        self.state = 152
                        localctx.right = self.oclExp(2)
                        pass

                    elif la_ == 15:
                        localctx = OclExpressionParser.CallExpressionContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.expression = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 153
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 154
                        self.argExp()
                        localctx.r = CANNOT_EVAL
                        pass

                    elif la_ == 16:
                        localctx = OclExpressionParser.MethodCallContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.expression = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 157
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 158
                        self.match(OclExpressionParser.T__1)
                        self.state = 159
                        localctx.attname = self.unrestrictedName()
                        self.state = 160
                        self.argExp()
                        localctx.r = CANNOT_EVAL
                        pass

                    elif la_ == 17:
                        localctx = OclExpressionParser.AttributeNavigationContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.expression = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 163
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 164
                        self.match(OclExpressionParser.T__1)
                        self.state = 165
                        localctx.attname = self.unrestrictedName()
                        localctx.r = CANNOT_EVAL
                        pass

                    elif la_ == 18:
                        localctx = OclExpressionParser.CollectionCallContext(self, OclExpressionParser.OclExpContext(self, _parentctx, _parentState))
                        localctx.expression = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_oclExp)
                        self.state = 168
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 169
                        self.match(OclExpressionParser.T__2)
                        self.state = 170
                        localctx.attname = self.unrestrictedName()
                        self.state = 171
                        self.argExp()
                        localctx.r = CANNOT_EVAL
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_argExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LambdaExpContext(ArgExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.ArgExpContext
            super().__init__(parser)
            self._unreservedName = None # UnreservedNameContext
            self.varnames = list() # of UnreservedNameContexts
            self.iterator = None # UnreservedNameContext
            self.initializer = None # OclExpContext
            self.body = None # OclExpContext
            self.copyFrom(ctx)

        def unreservedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.UnreservedNameContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.UnreservedNameContext,i)

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)

        def typeExpCS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.TypeExpCSContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.TypeExpCSContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExp" ):
                listener.enterLambdaExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExp" ):
                listener.exitLambdaExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExp" ):
                return visitor.visitLambdaExp(self)
            else:
                return visitor.visitChildren(self)


    class ArgumentsExpContext(ArgExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.ArgExpContext
            super().__init__(parser)
            self._oclExp = None # OclExpContext
            self.body = list() # of OclExpContexts
            self.copyFrom(ctx)

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentsExp" ):
                listener.enterArgumentsExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentsExp" ):
                listener.exitArgumentsExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentsExp" ):
                return visitor.visitArgumentsExp(self)
            else:
                return visitor.visitChildren(self)



    def argExp(self):

        localctx = OclExpressionParser.ArgExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_argExp)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = OclExpressionParser.ArgumentsExpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(OclExpressionParser.T__18)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4573616527824683006) != 0):
                    self.state = 180
                    localctx._oclExp = self.oclExp(0)
                    localctx.body.append(localctx._oclExp)
                    self.state = 185
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==20:
                        self.state = 181
                        self.match(OclExpressionParser.T__19)
                        self.state = 182
                        localctx._oclExp = self.oclExp(0)
                        localctx.body.append(localctx._oclExp)
                        self.state = 187
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 190
                self.match(OclExpressionParser.T__20)
                pass

            elif la_ == 2:
                localctx = OclExpressionParser.LambdaExpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(OclExpressionParser.T__18)
                self.state = 192
                localctx._unreservedName = self.unreservedName()
                localctx.varnames.append(localctx._unreservedName)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 193
                    self.match(OclExpressionParser.T__19)
                    self.state = 194
                    localctx._unreservedName = self.unreservedName()
                    localctx.varnames.append(localctx._unreservedName)
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 200
                    self.match(OclExpressionParser.T__21)
                    self.state = 201
                    self.typeExpCS()


                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 204
                    self.match(OclExpressionParser.T__22)
                    self.state = 205
                    localctx.iterator = self.unreservedName()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==22:
                        self.state = 206
                        self.match(OclExpressionParser.T__21)
                        self.state = 207
                        self.typeExpCS()


                    self.state = 210
                    self.match(OclExpressionParser.T__12)
                    self.state = 211
                    localctx.initializer = self.oclExp(0)


                self.state = 215
                self.match(OclExpressionParser.T__23)
                self.state = 216
                localctx.body = self.oclExp(0)
                self.state = 217
                self.match(OclExpressionParser.T__20)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None
            self.n_ = None # NestedExpContext
            self.n = None # PrimitiveLiteralExpContext

        def selfExp(self):
            return self.getTypedRuleContext(OclExpressionParser.SelfExpContext,0)


        def nestedExp(self):
            return self.getTypedRuleContext(OclExpressionParser.NestedExpContext,0)


        def primitiveLiteralExp(self):
            return self.getTypedRuleContext(OclExpressionParser.PrimitiveLiteralExpContext,0)


        def tupleLiteralExp(self):
            return self.getTypedRuleContext(OclExpressionParser.TupleLiteralExpContext,0)


        def collectionLiteralExp(self):
            return self.getTypedRuleContext(OclExpressionParser.CollectionLiteralExpContext,0)


        def typeLiteralExp(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeLiteralExpContext,0)


        def letExp(self):
            return self.getTypedRuleContext(OclExpressionParser.LetExpContext,0)


        def ifExp(self):
            return self.getTypedRuleContext(OclExpressionParser.IfExpContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_primaryExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExp" ):
                listener.enterPrimaryExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExp" ):
                listener.exitPrimaryExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExp" ):
                return visitor.visitPrimaryExp(self)
            else:
                return visitor.visitChildren(self)




    def primaryExp(self):

        localctx = OclExpressionParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_primaryExp)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.selfExp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                localctx.n_ = self.nestedExp()
                localctx.r = localctx.n_.r
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                localctx.n = self.primitiveLiteralExp()
                localctx.r = localctx.n.r
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.tupleLiteralExp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.collectionLiteralExp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.typeLiteralExp()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.letExp()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 232
                self.ifExp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelfExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_selfExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfExp" ):
                listener.enterSelfExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfExp" ):
                listener.exitSelfExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfExp" ):
                return visitor.visitSelfExp(self)
            else:
                return visitor.visitChildren(self)




    def selfExp(self):

        localctx = OclExpressionParser.SelfExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_selfExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(OclExpressionParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None
            self.nested = None # OclExpContext

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_nestedExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedExp" ):
                listener.enterNestedExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedExp" ):
                listener.exitNestedExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedExp" ):
                return visitor.visitNestedExp(self)
            else:
                return visitor.visitChildren(self)




    def nestedExp(self):

        localctx = OclExpressionParser.NestedExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nestedExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(OclExpressionParser.T__18)
            self.state = 238
            localctx.nested = self.oclExp(0)
            self.state = 239
            self.match(OclExpressionParser.T__20)
            localctx.r = localctx.nested.r
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveLiteralExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None


        def getRuleIndex(self):
            return OclExpressionParser.RULE_primitiveLiteralExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.r = ctx.r



    class StringLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.n = None # StringLiteralExpCSContext
            self.copyFrom(ctx)

        def stringLiteralExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.StringLiteralExpCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class BooleanLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.n = None # BooleanLiteralExpCSContext
            self.copyFrom(ctx)

        def booleanLiteralExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.BooleanLiteralExpCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteral" ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)


    class InvalidLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def invalidLiteralExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.InvalidLiteralExpCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidLiteral" ):
                listener.enterInvalidLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidLiteral" ):
                listener.exitInvalidLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvalidLiteral" ):
                return visitor.visitInvalidLiteral(self)
            else:
                return visitor.visitChildren(self)


    class UnlimitedNaturalLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unlimitedNaturalLiteralCS(self):
            return self.getTypedRuleContext(OclExpressionParser.UnlimitedNaturalLiteralCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlimitedNaturalLiteral" ):
                listener.enterUnlimitedNaturalLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlimitedNaturalLiteral" ):
                listener.exitUnlimitedNaturalLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnlimitedNaturalLiteral" ):
                return visitor.visitUnlimitedNaturalLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NullLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nullLiteralExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.NullLiteralExpCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLiteral" ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLiteral" ):
                listener.exitNullLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullLiteral" ):
                return visitor.visitNullLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NumberLiteralContext(PrimitiveLiteralExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveLiteralExpContext
            super().__init__(parser)
            self.n = None # NumberLiteralExpCSContext
            self.copyFrom(ctx)

        def numberLiteralExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.NumberLiteralExpCSContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLiteral" ):
                listener.enterNumberLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLiteral" ):
                listener.exitNumberLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLiteral" ):
                return visitor.visitNumberLiteral(self)
            else:
                return visitor.visitChildren(self)



    def primitiveLiteralExp(self):

        localctx = OclExpressionParser.PrimitiveLiteralExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitiveLiteralExp)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59, 60]:
                localctx = OclExpressionParser.NumberLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                localctx.n = self.numberLiteralExpCS()
                localctx.r = localctx.n.r
                pass
            elif token in [51, 52]:
                localctx = OclExpressionParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                localctx.n = self.booleanLiteralExpCS()
                localctx.r = (None if localctx.n is None else self._input.getText(localctx.n.start,localctx.n.stop)) == 'true'
                pass
            elif token in [56]:
                localctx = OclExpressionParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                localctx.n = self.stringLiteralExpCS()
                localctx.r = (None if localctx.n is None else self._input.getText(localctx.n.start,localctx.n.stop))
                pass
            elif token in [6]:
                localctx = OclExpressionParser.UnlimitedNaturalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.unlimitedNaturalLiteralCS()
                localctx.r = CANNOT_EVALUTATE
                pass
            elif token in [53]:
                localctx = OclExpressionParser.InvalidLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.invalidLiteralExpCS()
                localctx.r=None
                pass
            elif token in [54]:
                localctx = OclExpressionParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.nullLiteralExpCS()
                localctx.r=None
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleLiteralExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tupleLiteralPartCS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.TupleLiteralPartCSContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.TupleLiteralPartCSContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_tupleLiteralExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleLiteralExp" ):
                listener.enterTupleLiteralExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleLiteralExp" ):
                listener.exitTupleLiteralExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleLiteralExp" ):
                return visitor.visitTupleLiteralExp(self)
            else:
                return visitor.visitChildren(self)




    def tupleLiteralExp(self):

        localctx = OclExpressionParser.TupleLiteralExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tupleLiteralExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(OclExpressionParser.T__25)
            self.state = 263
            self.match(OclExpressionParser.T__26)
            self.state = 264
            self.tupleLiteralPartCS()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 265
                self.match(OclExpressionParser.T__19)
                self.state = 266
                self.tupleLiteralPartCS()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(OclExpressionParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleLiteralPartCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def primaryExp(self):
            return self.getTypedRuleContext(OclExpressionParser.PrimaryExpContext,0)


        def typeExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeExpCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_tupleLiteralPartCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleLiteralPartCS" ):
                listener.enterTupleLiteralPartCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleLiteralPartCS" ):
                listener.exitTupleLiteralPartCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleLiteralPartCS" ):
                return visitor.visitTupleLiteralPartCS(self)
            else:
                return visitor.visitChildren(self)




    def tupleLiteralPartCS(self):

        localctx = OclExpressionParser.TupleLiteralPartCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tupleLiteralPartCS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.unrestrictedName()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 275
                self.match(OclExpressionParser.T__21)
                self.state = 276
                self.typeExpCS()


            self.state = 279
            self.match(OclExpressionParser.T__12)
            self.state = 280
            self.primaryExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectionLiteralExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._collectionLiteralPartCS = None # CollectionLiteralPartCSContext
            self.expressions = list() # of CollectionLiteralPartCSContexts

        def collectionTypeCS(self):
            return self.getTypedRuleContext(OclExpressionParser.CollectionTypeCSContext,0)


        def collectionLiteralPartCS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.CollectionLiteralPartCSContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.CollectionLiteralPartCSContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_collectionLiteralExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionLiteralExp" ):
                listener.enterCollectionLiteralExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionLiteralExp" ):
                listener.exitCollectionLiteralExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionLiteralExp" ):
                return visitor.visitCollectionLiteralExp(self)
            else:
                return visitor.visitChildren(self)




    def collectionLiteralExp(self):

        localctx = OclExpressionParser.CollectionLiteralExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_collectionLiteralExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.collectionTypeCS()
            self.state = 283
            self.match(OclExpressionParser.T__26)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 284
                localctx._collectionLiteralPartCS = self.collectionLiteralPartCS()
                localctx.expressions.append(localctx._collectionLiteralPartCS)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 285
                    self.match(OclExpressionParser.T__19)
                    self.state = 286
                    localctx._collectionLiteralPartCS = self.collectionLiteralPartCS()
                    localctx.expressions.append(localctx._collectionLiteralPartCS)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 294
            self.match(OclExpressionParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectionTypeCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def collectionTypeIdentifier(self):
            return self.getTypedRuleContext(OclExpressionParser.CollectionTypeIdentifierContext,0)


        def typeExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeExpCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_collectionTypeCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionTypeCS" ):
                listener.enterCollectionTypeCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionTypeCS" ):
                listener.exitCollectionTypeCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionTypeCS" ):
                return visitor.visitCollectionTypeCS(self)
            else:
                return visitor.visitChildren(self)




    def collectionTypeCS(self):

        localctx = OclExpressionParser.CollectionTypeCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_collectionTypeCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.collectionTypeIdentifier()
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 297
                self.match(OclExpressionParser.T__18)
                self.state = 298
                self.typeExpCS()
                self.state = 299
                self.match(OclExpressionParser.T__20)

            elif la_ == 2:
                self.state = 301
                self.match(OclExpressionParser.T__8)
                self.state = 302
                self.typeExpCS()
                self.state = 303
                self.match(OclExpressionParser.T__9)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_primitiveTypeCS

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerType" ):
                listener.enterIntegerType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerType" ):
                listener.exitIntegerType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerType" ):
                return visitor.visitIntegerType(self)
            else:
                return visitor.visitChildren(self)


    class OCLMessageContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOCLMessage" ):
                listener.enterOCLMessage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOCLMessage" ):
                listener.exitOCLMessage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOCLMessage" ):
                return visitor.visitOCLMessage(self)
            else:
                return visitor.visitChildren(self)


    class OCLSelfContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOCLSelf" ):
                listener.enterOCLSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOCLSelf" ):
                listener.exitOCLSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOCLSelf" ):
                return visitor.visitOCLSelf(self)
            else:
                return visitor.visitChildren(self)


    class OCLVoidContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOCLVoid" ):
                listener.enterOCLVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOCLVoid" ):
                listener.exitOCLVoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOCLVoid" ):
                return visitor.visitOCLVoid(self)
            else:
                return visitor.visitChildren(self)


    class StringTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringType" ):
                listener.enterStringType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringType" ):
                listener.exitStringType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)


    class BooleanTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanType" ):
                listener.enterBooleanType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanType" ):
                listener.exitBooleanType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanType" ):
                return visitor.visitBooleanType(self)
            else:
                return visitor.visitChildren(self)


    class OCLAnyTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOCLAnyType" ):
                listener.enterOCLAnyType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOCLAnyType" ):
                listener.exitOCLAnyType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOCLAnyType" ):
                return visitor.visitOCLAnyType(self)
            else:
                return visitor.visitChildren(self)


    class OCLInvalidTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOCLInvalidType" ):
                listener.enterOCLInvalidType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOCLInvalidType" ):
                listener.exitOCLInvalidType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOCLInvalidType" ):
                return visitor.visitOCLInvalidType(self)
            else:
                return visitor.visitChildren(self)


    class RealTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealType" ):
                listener.enterRealType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealType" ):
                listener.exitRealType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealType" ):
                return visitor.visitRealType(self)
            else:
                return visitor.visitChildren(self)


    class UnlimitedNaturalTypeContext(PrimitiveTypeCSContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.PrimitiveTypeCSContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlimitedNaturalType" ):
                listener.enterUnlimitedNaturalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlimitedNaturalType" ):
                listener.exitUnlimitedNaturalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnlimitedNaturalType" ):
                return visitor.visitUnlimitedNaturalType(self)
            else:
                return visitor.visitChildren(self)



    def primitiveTypeCS(self):

        localctx = OclExpressionParser.PrimitiveTypeCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitiveTypeCS)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = OclExpressionParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(OclExpressionParser.T__28)
                pass
            elif token in [30]:
                localctx = OclExpressionParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(OclExpressionParser.T__29)
                pass
            elif token in [31]:
                localctx = OclExpressionParser.UnlimitedNaturalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.match(OclExpressionParser.T__30)
                pass
            elif token in [32]:
                localctx = OclExpressionParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(OclExpressionParser.T__31)
                pass
            elif token in [33]:
                localctx = OclExpressionParser.RealTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.match(OclExpressionParser.T__32)
                pass
            elif token in [34]:
                localctx = OclExpressionParser.OCLAnyTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 312
                self.match(OclExpressionParser.T__33)
                pass
            elif token in [35]:
                localctx = OclExpressionParser.OCLInvalidTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 313
                self.match(OclExpressionParser.T__34)
                pass
            elif token in [36]:
                localctx = OclExpressionParser.OCLMessageContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 314
                self.match(OclExpressionParser.T__35)
                pass
            elif token in [37]:
                localctx = OclExpressionParser.OCLSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 315
                self.match(OclExpressionParser.T__36)
                pass
            elif token in [38]:
                localctx = OclExpressionParser.OCLVoidContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 316
                self.match(OclExpressionParser.T__37)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectionTypeIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_collectionTypeIdentifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrderedSetTypeContext(CollectionTypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.CollectionTypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderedSetType" ):
                listener.enterOrderedSetType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderedSetType" ):
                listener.exitOrderedSetType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderedSetType" ):
                return visitor.visitOrderedSetType(self)
            else:
                return visitor.visitChildren(self)


    class SetTypeContext(CollectionTypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.CollectionTypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetType" ):
                listener.enterSetType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetType" ):
                listener.exitSetType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetType" ):
                return visitor.visitSetType(self)
            else:
                return visitor.visitChildren(self)


    class BagTypeContext(CollectionTypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.CollectionTypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBagType" ):
                listener.enterBagType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBagType" ):
                listener.exitBagType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBagType" ):
                return visitor.visitBagType(self)
            else:
                return visitor.visitChildren(self)


    class CollectionTypeContext(CollectionTypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.CollectionTypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionType" ):
                listener.enterCollectionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionType" ):
                listener.exitCollectionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionType" ):
                return visitor.visitCollectionType(self)
            else:
                return visitor.visitChildren(self)


    class SequenceTypeContext(CollectionTypeIdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OclExpressionParser.CollectionTypeIdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceType" ):
                listener.enterSequenceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceType" ):
                listener.exitSequenceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceType" ):
                return visitor.visitSequenceType(self)
            else:
                return visitor.visitChildren(self)



    def collectionTypeIdentifier(self):

        localctx = OclExpressionParser.CollectionTypeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_collectionTypeIdentifier)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                localctx = OclExpressionParser.CollectionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(OclExpressionParser.T__38)
                pass
            elif token in [40]:
                localctx = OclExpressionParser.BagTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(OclExpressionParser.T__39)
                pass
            elif token in [41]:
                localctx = OclExpressionParser.OrderedSetTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(OclExpressionParser.T__40)
                pass
            elif token in [42]:
                localctx = OclExpressionParser.SequenceTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.match(OclExpressionParser.T__41)
                pass
            elif token in [43]:
                localctx = OclExpressionParser.SetTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.match(OclExpressionParser.T__42)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectionLiteralPartCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.inf = None # OclExpContext
            self.isInterval = None # Token
            self.sup = None # OclExpContext

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_collectionLiteralPartCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectionLiteralPartCS" ):
                listener.enterCollectionLiteralPartCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectionLiteralPartCS" ):
                listener.exitCollectionLiteralPartCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectionLiteralPartCS" ):
                return visitor.visitCollectionLiteralPartCS(self)
            else:
                return visitor.visitChildren(self)




    def collectionLiteralPartCS(self):

        localctx = OclExpressionParser.CollectionLiteralPartCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_collectionLiteralPartCS)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.oclExp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                localctx.inf = self.oclExp(0)
                self.state = 328
                localctx.isInterval = self.match(OclExpressionParser.T__43)
                self.state = 329
                localctx.sup = self.oclExp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeLiteralExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeLiteralCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeLiteralCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_typeLiteralExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLiteralExp" ):
                listener.enterTypeLiteralExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLiteralExp" ):
                listener.exitTypeLiteralExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeLiteralExp" ):
                return visitor.visitTypeLiteralExp(self)
            else:
                return visitor.visitChildren(self)




    def typeLiteralExp(self):

        localctx = OclExpressionParser.TypeLiteralExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeLiteralExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.typeLiteralCS()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._letVariableCS = None # LetVariableCSContext
            self.variables = list() # of LetVariableCSContexts

        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)


        def letVariableCS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.LetVariableCSContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.LetVariableCSContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_letExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExp" ):
                listener.enterLetExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExp" ):
                listener.exitLetExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExp" ):
                return visitor.visitLetExp(self)
            else:
                return visitor.visitChildren(self)




    def letExp(self):

        localctx = OclExpressionParser.LetExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_letExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(OclExpressionParser.T__44)
            self.state = 336
            localctx._letVariableCS = self.letVariableCS()
            localctx.variables.append(localctx._letVariableCS)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 337
                self.match(OclExpressionParser.T__19)
                self.state = 338
                localctx._letVariableCS = self.letVariableCS()
                localctx.variables.append(localctx._letVariableCS)
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 344
            self.match(OclExpressionParser.T__45)
            self.state = 345
            self.oclExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetVariableCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def oclExp(self):
            return self.getTypedRuleContext(OclExpressionParser.OclExpContext,0)


        def typeExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeExpCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_letVariableCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetVariableCS" ):
                listener.enterLetVariableCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetVariableCS" ):
                listener.exitLetVariableCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetVariableCS" ):
                return visitor.visitLetVariableCS(self)
            else:
                return visitor.visitChildren(self)




    def letVariableCS(self):

        localctx = OclExpressionParser.LetVariableCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_letVariableCS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.unrestrictedName()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 348
                self.match(OclExpressionParser.T__21)
                self.state = 349
                self.typeExpCS()


            self.state = 352
            self.match(OclExpressionParser.T__12)
            self.state = 353
            self.oclExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeLiteralCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeLiteralCSContext,0)


        def typeNameExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeNameExpCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_typeExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpCS" ):
                listener.enterTypeExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpCS" ):
                listener.exitTypeExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpCS" ):
                return visitor.visitTypeExpCS(self)
            else:
                return visitor.visitChildren(self)




    def typeExpCS(self):

        localctx = OclExpressionParser.TypeExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_typeExpCS)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.typeLiteralCS()
                pass
            elif token in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 22, 23, 24, 27, 28, 44, 56, 57, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.typeNameExpCS(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def typeNameExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeNameExpCSContext,0)


        def unreservedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.UnreservedNameContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.UnreservedNameContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_typeNameExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeNameExpCS" ):
                listener.enterTypeNameExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeNameExpCS" ):
                listener.exitTypeNameExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeNameExpCS" ):
                return visitor.visitTypeNameExpCS(self)
            else:
                return visitor.visitChildren(self)



    def typeNameExpCS(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OclExpressionParser.TypeNameExpCSContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_typeNameExpCS, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.unrestrictedName()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OclExpressionParser.TypeNameExpCSContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_typeNameExpCS)
                    self.state = 362
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 365 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 363
                            self.match(OclExpressionParser.T__0)
                            self.state = 364
                            self.unreservedName()

                        else:
                            raise NoViableAltException(self)
                        self.state = 367 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
             
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeLiteralCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def collectionTypeCS(self):
            return self.getTypedRuleContext(OclExpressionParser.CollectionTypeCSContext,0)


        def primitiveTypeCS(self):
            return self.getTypedRuleContext(OclExpressionParser.PrimitiveTypeCSContext,0)


        def tupleTypeCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TupleTypeCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_typeLiteralCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLiteralCS" ):
                listener.enterTypeLiteralCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLiteralCS" ):
                listener.exitTypeLiteralCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeLiteralCS" ):
                return visitor.visitTypeLiteralCS(self)
            else:
                return visitor.visitChildren(self)




    def typeLiteralCS(self):

        localctx = OclExpressionParser.TypeLiteralCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typeLiteralCS)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.collectionTypeCS()
                pass
            elif token in [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.primitiveTypeCS()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.tupleTypeCS()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleTypeCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuplePartCS(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.TuplePartCSContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.TuplePartCSContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_tupleTypeCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleTypeCS" ):
                listener.enterTupleTypeCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleTypeCS" ):
                listener.exitTupleTypeCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleTypeCS" ):
                return visitor.visitTupleTypeCS(self)
            else:
                return visitor.visitChildren(self)




    def tupleTypeCS(self):

        localctx = OclExpressionParser.TupleTypeCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_tupleTypeCS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(OclExpressionParser.T__25)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(OclExpressionParser.T__18)
                self.state = 381
                self.tuplePartCS()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 382
                    self.match(OclExpressionParser.T__19)
                    self.state = 383
                    self.tuplePartCS()
                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 389
                self.match(OclExpressionParser.T__20)

            elif la_ == 2:
                self.state = 391
                self.match(OclExpressionParser.T__8)
                self.state = 392
                self.tuplePartCS()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 393
                    self.match(OclExpressionParser.T__19)
                    self.state = 394
                    self.tuplePartCS()
                    self.state = 399
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 400
                self.match(OclExpressionParser.T__9)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TuplePartCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unrestrictedName(self):
            return self.getTypedRuleContext(OclExpressionParser.UnrestrictedNameContext,0)


        def typeExpCS(self):
            return self.getTypedRuleContext(OclExpressionParser.TypeExpCSContext,0)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_tuplePartCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuplePartCS" ):
                listener.enterTuplePartCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuplePartCS" ):
                listener.exitTuplePartCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuplePartCS" ):
                return visitor.visitTuplePartCS(self)
            else:
                return visitor.visitChildren(self)




    def tuplePartCS(self):

        localctx = OclExpressionParser.TuplePartCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tuplePartCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.unrestrictedName()
            self.state = 405
            self.match(OclExpressionParser.T__21)
            self.state = 406
            self.typeExpCS()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None
            self.condition = None # OclExpContext
            self.body = None # OclExpContext
            self.else_ = None # OclExpContext

        def oclExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OclExpressionParser.OclExpContext)
            else:
                return self.getTypedRuleContext(OclExpressionParser.OclExpContext,i)


        def getRuleIndex(self):
            return OclExpressionParser.RULE_ifExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExp" ):
                listener.enterIfExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExp" ):
                listener.exitIfExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExp" ):
                return visitor.visitIfExp(self)
            else:
                return visitor.visitChildren(self)




    def ifExp(self):

        localctx = OclExpressionParser.IfExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(OclExpressionParser.T__46)
            self.state = 409
            localctx.condition = self.oclExp(0)
            self.state = 410
            self.match(OclExpressionParser.T__47)
            self.state = 411
            localctx.body = self.oclExp(0)
            self.state = 412
            self.match(OclExpressionParser.T__48)
            self.state = 413
            localctx.else_ = self.oclExp(0)
            self.state = 414
            self.match(OclExpressionParser.T__49)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberLiteralExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.r = None
            self._INT = None # Token
            self._FLOAT = None # Token

        def INT(self):
            return self.getToken(OclExpressionParser.INT, 0)

        def FLOAT(self):
            return self.getToken(OclExpressionParser.FLOAT, 0)

        def getRuleIndex(self):
            return OclExpressionParser.RULE_numberLiteralExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLiteralExpCS" ):
                listener.enterNumberLiteralExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLiteralExpCS" ):
                listener.exitNumberLiteralExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLiteralExpCS" ):
                return visitor.visitNumberLiteralExpCS(self)
            else:
                return visitor.visitChildren(self)




    def numberLiteralExpCS(self):

        localctx = OclExpressionParser.NumberLiteralExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_numberLiteralExpCS)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                localctx._INT = self.match(OclExpressionParser.INT)
                localctx.r=int((None if localctx._INT is None else localctx._INT.text))
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                localctx._FLOAT = self.match(OclExpressionParser.FLOAT)
                localctx.r=float((None if localctx._FLOAT is None else localctx._FLOAT.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(OclExpressionParser.STRING, 0)

        def getRuleIndex(self):
            return OclExpressionParser.RULE_stringLiteralExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteralExpCS" ):
                listener.enterStringLiteralExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteralExpCS" ):
                listener.exitStringLiteralExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteralExpCS" ):
                return visitor.visitStringLiteralExpCS(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteralExpCS(self):

        localctx = OclExpressionParser.StringLiteralExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stringLiteralExpCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(OclExpressionParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_booleanLiteralExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteralExpCS" ):
                listener.enterBooleanLiteralExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteralExpCS" ):
                listener.exitBooleanLiteralExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteralExpCS" ):
                return visitor.visitBooleanLiteralExpCS(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteralExpCS(self):

        localctx = OclExpressionParser.BooleanLiteralExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_booleanLiteralExpCS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not(_la==51 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnlimitedNaturalLiteralCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_unlimitedNaturalLiteralCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlimitedNaturalLiteralCS" ):
                listener.enterUnlimitedNaturalLiteralCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlimitedNaturalLiteralCS" ):
                listener.exitUnlimitedNaturalLiteralCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnlimitedNaturalLiteralCS" ):
                return visitor.visitUnlimitedNaturalLiteralCS(self)
            else:
                return visitor.visitChildren(self)




    def unlimitedNaturalLiteralCS(self):

        localctx = OclExpressionParser.UnlimitedNaturalLiteralCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_unlimitedNaturalLiteralCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(OclExpressionParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidLiteralExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_invalidLiteralExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidLiteralExpCS" ):
                listener.enterInvalidLiteralExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidLiteralExpCS" ):
                listener.exitInvalidLiteralExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvalidLiteralExpCS" ):
                return visitor.visitInvalidLiteralExpCS(self)
            else:
                return visitor.visitChildren(self)




    def invalidLiteralExpCS(self):

        localctx = OclExpressionParser.InvalidLiteralExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_invalidLiteralExpCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(OclExpressionParser.T__52)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullLiteralExpCSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_nullLiteralExpCS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullLiteralExpCS" ):
                listener.enterNullLiteralExpCS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullLiteralExpCS" ):
                listener.exitNullLiteralExpCS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullLiteralExpCS" ):
                return visitor.visitNullLiteralExpCS(self)
            else:
                return visitor.visitChildren(self)




    def nullLiteralExpCS(self):

        localctx = OclExpressionParser.NullLiteralExpCSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_nullLiteralExpCS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(OclExpressionParser.T__53)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnrestrictedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_unrestrictedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnrestrictedName" ):
                listener.enterUnrestrictedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnrestrictedName" ):
                listener.exitUnrestrictedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnrestrictedName" ):
                return visitor.visitUnrestrictedName(self)
            else:
                return visitor.visitChildren(self)




    def unrestrictedName(self):

        localctx = OclExpressionParser.UnrestrictedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unrestrictedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 72040001418788896) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnreservedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OclExpressionParser.RULE_unreservedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnreservedName" ):
                listener.enterUnreservedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnreservedName" ):
                listener.exitUnreservedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnreservedName" ):
                return visitor.visitUnreservedName(self)
            else:
                return visitor.visitChildren(self)




    def unreservedName(self):

        localctx = OclExpressionParser.UnreservedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unreservedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            _la = self._input.LA(1)
            if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 35993612683542560) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.oclExp_sempred
        self._predicates[17] = self.typeNameExpCS_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def oclExp_sempred(self, localctx:OclExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 17)
         

    def typeNameExpCS_sempred(self, localctx:TypeNameExpCSContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         




