import pytest
from string_calculator import string_calculator

def test_add_empty_string():
   calc = string_calculator()
   assert calc.add("") == 0 

def test_add_single_number():
   cal = string_calculator()
   assert cal.add("1") == 1
   assert cal.add("2") == 2