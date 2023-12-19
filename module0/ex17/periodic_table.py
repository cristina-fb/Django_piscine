import sys

def create_table_headers(f):
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"en\">\n")
    f.write("<head>\n")
    f.write("\t<meta charset=\"UTF-8\">\n")
    f.write("\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    f.write("\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write("\t<title>Periodic Table!</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("\t<h1 align=\"center\">PERIODIC TABLE OF ELEMENTS ⚛️ </h1>\n")
    f.write("\t<table>\n")

def create_table_rows(dic, f):
    C1 = "background-color: rgb(214, 240, 180);\">\n"
    C2 = "background-color: rgb(172, 120, 145);\">\n"
    C3 = "background-color: rgb(224, 231, 172);\">\n"
    C4 = "background-color: rgb(220, 180, 134);\">\n"
    C5 = "background-color: rgb(233, 220, 159);\">\n"
    C6 = "background-color: rgb(192, 154, 138);\">\n"
    C7 = "background-color: rgb(147, 163, 172);\">\n"
    C8 = "background-color: rgb(134, 195, 195);\">\n"
    last = 0
    for key, value in dic.items():
        if value[0] == '0':
            last = 0
            f.write("\t\t<tr>\n")
        if int(value[0]) - last != 0:
            for i in range(int(value[0]) - last):
                f.write("\t\t\t<td></td>\n")
            last = int(value[0]) + 1
        else:
            last += 1
        if int(value[0]) > 1 and int(value[0]) < 12:
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C1)
        elif value[0] == '1':
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C2)
        elif value[0] == '16':
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C3)
        elif value[0] == '17':
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C4)
        elif value[0] == '0' and int(key) > 1:
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C5)
        elif key == '1' or key == '6' or key == '7' or key == '8' or key == '15' or key == '16' or key == '34':
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C6)
        elif key == '5' or key == '14' or key == '32' or key == '33' or key == '51' or key == '52' or key == '84':
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C7)
        else:
            f.write("\t\t\t<td style=\"border: 1px solid black;" + C8)
        f.write("\t\t\t\t<ul style=\"list-style: none;\">\n")
        f.write("\t\t\t\t\t<li>" + key + "</li>\n")
        f.write("\t\t\t\t\t<li><h2 style=\"margin: 0;\">" + value[1] + "</h2></li>\n")
        f.write("\t\t\t\t\t<li>" + value[2] + "</li>\n")
        f.write("\t\t\t\t\t<li>E: " + value[3] + "</li>\n")
        f.write("\t\t\t\t</ul>\n")
        f.write("\t\t\t</td>\n")
        if value[0] == '17':
            f.write("\t\t</tr>\n")

def create_table_end(f):
    f.write("\t</table>\n")
    f.write("</body>\n")
    f.write("</html>\n")

def create_dict(text):
    dic = {}
    for i in text.split("\n"):
        values = []
        for j in i.split(","):
            values.append(j[j.find(":") + 1 :])
        key = values[1]
        values.remove(key)
        dic[key] = values
    return(dic)
        
def read_file():
    f = open("periodic_table.txt", "r")
    return f.read()

if __name__ == '__main__':
    text = read_file()
    dic = create_dict(text)
    htmlf = open("periodic_table.html", "a")
    create_table_headers(htmlf)
    create_table_rows(dic, htmlf)
    create_table_end(htmlf)