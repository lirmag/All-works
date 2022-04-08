import re
with open("24_demo (3).txt") as f:
    txt = f.read()
    print(max((len(s) for s in re.findall(r"X(?:YZX)*(?:YZ?)?", txt)), default=0))
