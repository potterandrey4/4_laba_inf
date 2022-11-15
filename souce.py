f = open('s.xml', encoding='utf-8')
xml = []
for line in f:
    l = line
    while "\t" in l:
        l = l.replace("\t", "", 1)
        l = l.replace("\n", "", 1)

    xml.append(l)


json = '{\n'


def string_with_params(st):
    res = ''
    t = st.replace('<', '', 1).replace('>', '', 1).split(' ')
    for el in t[1:]:
        t = el.split('=')
        res += ('"@' + t[0] + '"' + ': ' + t[1] + ",\t")
    return res


def st_to_json(st):
    t = (st.replace('</', '  ').replace('>', '  ').replace('<', '')).split('  ')
    t = t[:len(t)-2]
    res = '\n"' + t[0] + '": "' + ''.join(t[1:]) + '",'
    return res

t1 = t2 = 0
for i in xml:
    if i == '<LESSON>':
        if t1 == 0:
            json += '\n"LESSON": [\n{'
        if t1 == 1:
            json = json[:-1] + '\n},\n{'
        t1 += 1
    if i == '</LESSON>':
        if t2 == 0:
            t2 += 1
        else:
            json = json[:-1] + '\n}\n]'

    if '</' not in i:
        if i.isupper:
            if i.count(" ") > 0:
                json += '"' + i.split(" ")[0].replace('<', '', 1) + '": { '
                json += string_with_params(i)

        if i.count(" ") == 0 and i.count('LESSON') == 0:
            json += i.replace("<", '"').replace('>', '": {')

    elif i.count(" ") > 0:
        json += st_to_json(i)
json += '\n}\n}\n}'
#print()
#print(json)