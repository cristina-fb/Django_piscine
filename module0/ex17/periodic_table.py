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
    f.write("\t<table>\n")

def create_table_rows(dic, f):
    last = 0
    for key, value in dic.items():
        if value[0] == '0':
            f.write("\t\t<tr>\n")
        if (int(value[0]) == 0) or (int(value[0]) - last == 1):
            f.write("\t\t\t<td style=\"border: 1px solid black;\">\n")
            f.write("\t\t\t\t<ul style=\"list-style: none;\">\n")
            f.write("\t\t\t\t\t<li>" + key + "</li>\n")
            f.write("\t\t\t\t\t<li><h2 style=\"margin: 0;\">" + value[1] + "</h2></li>\n")
            f.write("\t\t\t\t\t<li>" + value[2] + "</li>\n")
            f.write("\t\t\t\t\t<li>E: " + value[3] + "</li>\n")
            f.write("\t\t\t\t</ul>\n")
            f.write("\t\t\t</td>\n")
        else:
            for i in range(int(value[0]) - last):
                f.write("\t\t\t<td style=\"border: 1px solid black;\"></td>\n")
        if value[0] == '17':
            f.write("\t\t</tr>\n")
            last = 0
    last = int(value[0])

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