# Задача. Реализуйте RLE алгоритм: используйте модуль сжатия и восстановления данных.
#         Входные и выходные данные хранятся в отдельных текстовых файлах. 
#         aaaabbbccccc -> 4a3b5c
#         4a3b5c -> aaaabbbccccc

text = 'aaaaaabbbbbccccccccdddddd'
compr_text = '10a9d15c'

def compression(text):
    compress = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        compress += str(count) + text[i]
        i = i + 1
    return compress

def unpacking(text: str) -> str:
    new_string = ''
    string_list = []
    digit = ''
    for i in range(len(text)):
        if text[i].isdigit():
            digit += text[i]
        else:
            if digit:
                string_list.append(digit)
            string_list.append(text[i])
            digit = ''
    for i in range(len(string_list) - 1):
        if string_list[i].isdigit():
            new_string += string_list[i + 1] * (int(string_list[i])- 1)
        else:
            new_string += string_list[i]
    new_string += text[-1]
    return new_string
print(compression(text))
print(unpacking(compr_text))