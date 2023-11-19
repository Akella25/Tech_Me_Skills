from datetime import datetime
#((lambda x: 'четное' if x % 2 == 0 else 'не четное')(10))

#arr = [1, 2, 3, 4, 5, 6]
#print(list(map(lambda x:  str(x), range(1, 7))))


#arr = ('имамами', 'имашами', 'итти', 'ищущи', 'машина', 'жаба')
#def revers_tru(x):
#   return x == x[::-1]
#print(tuple(filter(revers_tru, ('имамами', 'имашами', 'итти', 'ищущи', 'машина', 'жаба'))))



def time_sek(funk):
    def wrraper(*arg, **qwarg):
        time = datetime.now()
        a = funk(*arg, **qwarg)
        time1 = datetime.now()
        res = time1 - time
        print(res)
        return  a

    return wrraper

@time_sek
def faktorial(num):
    if num == 1:
        return num

    return num * faktorial(num - 1)


arr = ['имамами', 'имашами', 'итти', 'ищущи', 'машина', 'жаба']

@time_sek
def revers_tru(x):

    return x == x[::-1]


rev = revers_tru(arr)
print(rev)

f = faktorial(5)
print(f)


def digit(text):
    num_str = []

    for i in text:
        if i.isalpha():
          return f'Вы ввели не корректное число: {text}'
        exit
    if not text.isdigit():

        if '-' in text and '.' not in text:
            for i in text:
                num_str.append(i)
            new_list = ''.join(num_str)
            return f'Вы ввели отрицательное целое число: {new_list}'
        if '.' in text and '-' not in text:
            for i in text:
                num_str.append(i)
            new_list = ''.join(num_str)

            return f'Вы ввели дробное число:{float(new_list)}'

        if '-' in text and '.' in text:
            for i in text:
                num_str.append(i)
            new_list = ''.join(num_str)

            return f'Вы ввели отрицательное дробное число:{float(new_list)}'


        return f'Вы ввели положительное целое число: {int(text)}'


a = input()
print(digit(a))

