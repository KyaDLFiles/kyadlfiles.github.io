"""
To save time, I made this script that allows to do this in the HTML files:
Write #@ followed by the button as it is called in /common/btn/, without the .png
Eg: #@o for circle
Then, run this script and supply it the html file path, and it will replace all of the patterns with the corresponding img element for that button
Bc I'm lazy, this will not alter the original file and will instead create a new one, so remember that!
"""

from sys import argv

if (len(argv) < 2):
    fp = input("File path: ")
else:
    fp = argv[1]

fin = open(fp, "r", encoding="utf-8")
fout = open(fp + "2.html", "w", encoding="utf-8")
btns = {
    "st": "Start",
    "se": "Select",
    "dd": "D-pad down",
    "dr": "D-pad right",
    "du": "D-pad up",
    "dl": "D-pad left",
    "r2": "R2",
    "l2": "L2",
    "r1": "R1",
    "l1": "L1",
    "r3": "R3",
    "l3": "L3",
    "x": "X", 
    "o": "Circle",
    "t": "Triangle",
    "s": "Square", #Square at the end bc of st and se
}

for line in fin:
    if "#@" in line:
        print(line)
        for i in btns:
            line = line.replace("#@" + i, f'<img src="/common/btn/{i}.png" alt="{btns[i]}">')
    
    fout.write(line)
    