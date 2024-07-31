import re
class string_calculator:
   def add(self, numbers : str) -> int:
      """Add numbers in a string
      
      Arguments:
      string : numbers -- string containing numbers separated by commas or new lines or custom delimiters
      Return: int -- sum of the numbers in the string
      """
      
      
      # Check if the string is empty
      if not numbers:
         return 0
      
      
      # initialize the delimiter
      delimiter = ','
      
      
      # split the string into delimiter and numbers
      delimiter , numbers = self.__find_delimiter(numbers)
      
      
      # convert the string to a list of integers
      integers_to_add = self.__convert_string_to_integers(numbers, delimiter)
      
      
      
      # check if there are negative numbers in the list
      self.__check_negative_numbers(integers_to_add)
      
      integers_to_add = self.__ignore_numbers_greater_than_1000(integers_to_add)
      
      # return the sum of the numbers
      return sum(integers_to_add)
   
   def __find_delimiter(self, numbers : str) -> list:
      """Find the delimiter in the string
      
      Arguments:
      string : numbers -- string containing numbers separated by commas or new lines or custom delimiters
      Return: ist -- list containing delimiter and numbers
      """
      
      delimiter=','
      
      # Check if the string starts with a custom delimiter
      if numbers.startswith("//"):
         # Split the string into delimiter and numbers on the first new line
         delimiter_part, numbers = numbers.split("\n", 1)
         delimiter = delimiter_part[2:]
         
         if delimiter == "":
            delimiter = "\n"
      
      return [delimiter, numbers]

   def __convert_string_to_integers(self, numbers, delimiter = ',') -> list:
      """Convert the string to a list of integers
      
      Arguments:
      string : numbers -- list of strings
      Return: list -- list of integers
      """
      
      
      # Replace new lines with delimiters
      if delimiter != "\n":
         numbers = numbers.replace("\n", delimiter)
      
      # Split the numbers into a list
      integers_to_add= re.split(re.escape(delimiter), numbers)
      integers = []
      invalid_inputs = []
      
      # Check if the numbers are valid integers
      for number in integers_to_add.copy():
         number = number.strip()
         if number == '':
            continue
         if re.match(r'^-?\d+$', number):
            integers.append(int(number))
         else:
            invalid_inputs.append(number)
   
      
      # Raise an error if there are invalid inputs
      if invalid_inputs:
         raise ValueError(f"invalid input: {', '.join(invalid_inputs)}")
      
      return integers
   
   
   def __check_negative_numbers(self, integers_to_add : list):
      """Check if there are negative numbers in the list
      
      Arguments:
      list : integers_to_add -- list of integers
      """
      
      # list of negative numbers
      negative_numbers = [number for number in integers_to_add if number < 0]

      
      # Raise an error if there are negative numbers
      if negative_numbers:
         raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
   
   def __ignore_numbers_greater_than_1000(self, integers_to_add : list) -> list:
      """Ignore numbers greater than 1000
      
      Arguments:
      list : integers_to_add -- list of integers
      Return: list -- list of integers
      """
      
      return [number for number in integers_to_add if number <= 1000]