import sys, re, os
from settings import *

if len(sys.argv) == 2:
    f = open("myCV.template","r")
    template = f.read()
    x = re.sub(**globals(),"\{(.*)\}", template)
    # matches = re.findall("\{(.*)\}",template)
    # for i in matches:
    #     template = template.replace()
    f = open("myCV.html","a")
    f.write(template)