import pytest
from string_calculator import string_calculator

def test_add_empty_string():
   calc = string_calculator()
   assert calc.add("") == 0 