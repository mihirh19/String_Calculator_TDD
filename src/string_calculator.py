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
      
      
      # Check if the string starts with a custom delimiter
      if numbers.startswith("//"):
         # Split the string into delimiter and numbers on the first new line
         delimiter_part, numbers = numbers.split("\n", 1)
         delimiter = delimiter_part[2:]
         
         if delimiter == "":
            delimiter = "\n"
      
      # Replace new lines with delimiters
      if delimiter != "\n":
         numbers = numbers.replace("\n", delimiter)
      
      
      # Split the numbers into a list
      integers_to_add= re.split(re.escape(delimiter), numbers)
      integers = []
      invalid_inputs =[]
      
      # Check if the numbers are valid integers
      for number in integers_to_add.copy():
         number = number.strip()
         if number == '':
            continue
         if re.match(r'^-?\d+$', number):
            integers.append(int(number))
         else:
            invalid_inputs.append(number)
      integers_to_add = integers
      
      # Raise an error if there are invalid inputs
      if invalid_inputs:
         raise ValueError(f"invalid input: {', '.join(invalid_inputs)}")
      
      
      
      # list of negative numbers
      negative_numbers = [number for number in integers_to_add if number < 0]

      
      # Raise an error if there are negative numbers
      if negative_numbers:
         raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
      
      # return the sum of the numbers
      return sum(integers_to_add)