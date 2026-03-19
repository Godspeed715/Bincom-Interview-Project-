import re
with open("baby2008.html") as file:
    html = file.read()
    data = re.findall(r'<td>([^0-9]+?)</td>', html)
    print(data)