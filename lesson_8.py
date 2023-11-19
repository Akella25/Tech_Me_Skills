# text = b'r\xc3\xa9sum\xc3\xa9'

# print(b:=text.decode('utf-8'))
# print(c:=b.encode('latin1'))
# print(d:=c.decode('latin1'))


# s1, s2, s3, s4 = input(), input(), input(), input()
#
# f = open('text.txt', 'w')
# f.write(f'{s1} \n{s2}\n')
# f.close()
#
# f = open('text.txt', 'a')
# f.write(f'{s3} \n{s4}')
# f.close()

#
import json

dict1 = {123456: ('Johan', 22), 123457: ('lui', 33),
         123458: ('zun', 44), 123459: ('lulu', 55),
         123465: ('Si', 66), 123478: ('jak', 77)}

with open('text.json', 'w') as file:
    json.dump(dict1, file)

import csv

with open('text.json') as file_2:
    json_file = json.load(file_2)

phone_arr = ['999999', '9999999', '9999', '999', '99', '999']

for i, y in zip(json_file, phone_arr):
    json_file[i].append(y)


with open('test.csv', 'w') as file_1:
    writer = csv.writer(file_1)

    writer.writerow(('id', 'name', 'age', 'phone'))

for key in json_file:
    id1 = key
    name = json_file[key][0]
    age = json_file[key][1]
    phone = json_file[key][2]

    with open('test.csv', 'a') as file_1:
        writer = csv.writer(file_1)
        writer.writerow((id1, name, age, phone))

import csv

with open('test.csv', 'r') as file3:
    writer = csv.DictReader(file3)
    for i in writer:
        print(i)