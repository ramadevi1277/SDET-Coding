import re


def camel_casing(words):
    camel_casing_list = []
    for word in words:
        list_words = re.split(r'-|_', word)
        camel_casing_word = list_words[0] + ''.join(map(lambda x: x.title(), list_words[1:]))
        camel_casing_list.append(camel_casing_word)
    print(camel_casing_list)



camel_casing(['Python_programming', 'codingInterview-test', "python-pogramming_life"])

