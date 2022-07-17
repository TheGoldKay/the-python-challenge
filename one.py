#### http://www.pythonchallenge.com/pc/def/map.html

import enum
from string import ascii_lowercase as alpha

"""
  K -> M
  O -> Q
  E -> G
"""

def get_map():
  m1 = dict()
  m2 = dict()
  for i, c in enumerate(alpha):
    m1[c] = i
    m2[i] = c 
  return m1, m2

char2num, num2char = get_map()

def dif(c1, c2):
  return char2num[c2] - char2num[c1]

print(dif('k', 'm'))
print(dif('o', 'q'))
print(dif('e', 'g'))

def mapping(s):
  news = ""
  for i, c in enumerate(s):
    newc = c 
    if newc.isalpha():
      newc = char2num[c] + 2
      #print(newc)
      newc = newc%26
      newc = num2char[newc]
    news += newc 
  return news 

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
print(mapping("map"))