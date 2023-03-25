#!/usr/bin/env python3

import re

class MyString:
  
  def __init__(self, sentence=''):
    self.__value = ''
    self.sentence = sentence
    
        
  def setvalue(self, value): 
    if type(value) == str:
      self.__value=value
    else:
      print("The value must be a string.")
        
  def getvalue(self):
    print('getname() called')
    return self.__value
  
  value=property(getvalue, setvalue)
  
  # Resource on how to create a property on Python Class: https://www.tutorialsteacher.com/python/python-class
  
  def is_sentence(self):
    return self.sentence.endswith(".")
  
  def is_question(self):
    return self.sentence.endswith("?")
  
  def is_exclamation(self):
    return self.sentence.endswith("!")
  
  def count_sentences(self):
    a = self.sentence.replace("...", '').replace('.', '*').replace("!", '*').replace('?', '*')
    a = a.split("*")
    return len(a) - 1
    
    # Resource: https://datagy.io/python-split-string-multiple-delimiters/
    # Resource: https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
    # split_string = re.split(r'[.|!|?]', self.sentence)
    # return split_string.count
    pass




    
  
