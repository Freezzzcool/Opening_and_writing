dict_ = {}
qwt_ = {}

with open('1.txt', encoding='utf-8') as file1:
    list1 = file1.readlines()
    dict_['1.txt'] = list1
    qwt_[len(list1)] = '1.txt'

with open('2.txt', encoding='utf-8') as file2:
    list2 = file2.readlines()
    dict_['2.txt'] = list2
    qwt_[len(list2)] = '2.txt'

with open('3.txt', encoding='utf-8') as file3:
    list3 = file3.readlines()
    dict_['3.txt'] = list3
    qwt_[len(list3)] = '3.txt'


sort_ = dict(sorted(qwt_.items(), key=lambda item: item[0]))

with open('4.txt', 'w') as file:
    for key, value in sort_.items():
        put = str(value) + '\n' + str(key) + '\n' + "".join(dict_.get(value)) + '\n'
        file.write(put)
