import xmltodict, json

f = open('s.xml', encoding='UTF-8')
xml = []
for line in f:
    t = line
    while "\t" in t or "\n" in t:
        t = t.replace("\t", "", 1)
        t = t.replace("\n", "", 1)

    xml.append(t)
source = "".join(xml)
o = xmltodict.parse(source)
res = json.dumps(o)
print(res.encode().decode('unicode-escape'))
