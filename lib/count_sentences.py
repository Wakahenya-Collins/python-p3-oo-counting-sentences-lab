#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
    # Split the value using '.', '?', and '!' as delimiters
      sentences = re.split(r'[.?!]', self.value)
    # Count the non-empty strings (sentences)
      num_sentences = len([sentence for sentence in sentences if sentence.strip()])
      
      return num_sentences


string = MyString()
string.value = "This is a string! It has three sentences. Right?"

print(string.is_sentence())    # Output: False
print(string.is_question())    # Output: False
print(string.is_exclamation()) # Output: True
print(string.count_sentences()) # Output: 3
