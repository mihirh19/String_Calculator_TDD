import pytest
from string_calculator import string_calculator

def test_add_empty_string():
   calc = string_calculator()
   assert calc.add("") == 0 

def test_add_single_number():
   cal = string_calculator()
   assert cal.add("1") == 1
   assert cal.add("2") == 2

def test_add_two_numbers():
   cal = string_calculator()
   assert cal.add("1,2") == 3
   assert cal.add("5,4") == 9

def test_add_three_numbers():
   cal = string_calculator()
   assert cal.add("1,2,3") == 6
   assert cal.add("5,4,3") == 12

def test_add_many_numbers():
   cal = string_calculator()
   assert cal.add("1,2,3,4,5") == 15
   assert cal.add("5,4,3,2,1") == 15
   
def test_add_newline_delimiter():
   cal = string_calculator()
   assert cal.add("1\n2,3") == 6
   assert cal.add("5\n4\n3") == 12