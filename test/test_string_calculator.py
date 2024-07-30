import pytest
from string_calculator import string_calculator



def test_add_empty_string():
   """Test  case for empty string returns 0."""
   calc = string_calculator()
   assert calc.add("") == 0 

def test_add_single_number():
   """Test case for single number returns the number."""
   cal = string_calculator()
   assert cal.add("1") == 1
   assert cal.add("2") == 2

def test_add_two_numbers():
   """Test case for two numbers returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("1,2") == 3
   assert cal.add("5,4") == 9

def test_add_three_numbers():
   """Test case for three numbers returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("1,2,3") == 6
   assert cal.add("5,4,3") == 12

def test_add_many_numbers():
   """Test case for many numbers returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("1,2,3,4,5") == 15
   assert cal.add("5,4,3,2,1") == 15
   
def test_add_newline_delimiter():
   """Test case for new line delimiter returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("1\n2,3") == 6
   assert cal.add("5\n4\n3") == 12

def test_add_custom_delimiter():
   """Test case for custom delimiter returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("//;\n1;2") == 3
   assert cal.add("//;\n5;4\n3") == 12

def test_add_custom_delimiter2():
   """Test case for custom delimiter with length > 1  returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("//|\n1|2") == 3
   assert cal.add("//|\n5|4\n3") == 12
   assert cal.add("//**\n5**4\n3**2") == 14

def test_add_negative_numbers():
   """Test case for negative numbers raises an error."""
   cal = string_calculator()
   with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
      cal.add("-1")
   with pytest.raises(ValueError, match="negative numbers not allowed: -1, -3, -4"):
      cal.add('-1,-3,-4,6')

def test_add_custom_delimiter_with_newline():
   """Test case for custom delimiter with newline returns the sum of the numbers."""
   cal = string_calculator()
   assert cal.add("//\n\n1\n2\n3") == 6

def test_non_numeric_characters():
   """Test case for non-numeric characters raises an error."""
   cal = string_calculator()
   with pytest.raises(ValueError, match="invalid input: a"):
      cal.add("1,a")