import json
from json2html import *


with open ('input1.json') as f:
    d = json.load(f)
    scanOutput =json2html.convert(json=d)
    htmlReportFile = "outfile.html"
    with open(htmlReportFile,'w') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("successfully convrted")
