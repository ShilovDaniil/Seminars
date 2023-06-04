dictionary = {}
dictionary = [{"V": "S001"}, {"V":"SOO2"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
list = set()
for i in dictionary:
    for j in i.keys():
        list.add(i[j].strip())
print(list)