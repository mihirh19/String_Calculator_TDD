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

def test_add_custom_delimiter():
   cal = string_calculator()
   assert cal.add("//;\n1;2") == 3
   assert cal.add("//;\n5;4\n3") == 12

def test_add_custom_delimiter2():
   cal = string_calculator()
   assert cal.add("//|\n1|2") == 3
   assert cal.add("//|\n5|4\n3") == 12
   assert cal.add("//**\n5**4\n3**2") == 14

def test_add_negative_numbers():
   cal = string_calculator()
   with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
      cal.add("-1")
   with pytest.raises(ValueError, match="negative numbers not allowed: -1, -3, -4"):
      cal.add('-1,-3,-4,6')

def test_add_custom_delimiter_with_newline():
   cal = string_calculator()
   assert cal.add("//\n\n1\n2\n3") == 6