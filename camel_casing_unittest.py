import re
import unittest


def camel_casing(words):
    camel_casing_list = []
    for word in words:
        list_words = re.split(r'-|_', word)
        camel_casing_word = list_words[0] + ''.join(map(lambda x: x.title(), list_words[1:]))
        camel_casing_list.append(camel_casing_word)
        return camel_casing_list

class TestCamelCasing(unittest.TestCase):
    def test_camel_casing(self):
        words_camel = ['python_programming', 'codingInterview-test', 'python-pogramming_life']
        for each in camel_casing(words_camel):
            self.assertTrue(each[0].islower(), f"{each} is not a camel case")

    def test_pascal_casing(self):
        words_pascal = ['Python_programming', 'CodingInterview-test', 'Python-pogramming_life']
        for each in camel_casing(words_pascal):
            self.assertTrue(each[0].isupper(), f"{each} is not a pascal case")


if __name__ == '__main__':
    unittest.main()



