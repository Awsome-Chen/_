from Parser import Parser
from Show import Show
from day import check,update


if check():
    exit()
p = Parser()
p.parse()
divs = p.school_title_divs + p.depart_title_divs
for div in divs:
    if "转专业" in div:
        Show("内容中包含转专业")
        update()
        exit()
    else:
        Show("内容中不包含转专业")
        update()
        exit()