import re
class string_calculator:
   def add(self, numbers : str) -> int:
      if not numbers:
         return 0
      delimiter = ','

      if numbers.startswith("//"):
         delimiter_part, numbers = numbers.split("\n", 1)
         delimiter = delimiter_part[2:]
         if delimiter == "":
            delimiter = "\n"
      
      # Replace new lines with delimiters
      if delimiter != "\n":
         numbers = numbers.replace("\n", delimiter)
      
      integers_to_add= re.split(re.escape(delimiter), numbers)
      integers = []
      invalid_inputs =[]
      for number in integers_to_add.copy():
         number = number.strip()
         if number == '':
            continue
         if re.match(r'^-?\d+$', number):
            integers.append(int(number))
         else:
            invalid_inputs.append(number)
      integers_to_add = integers
      if invalid_inputs:
         raise ValueError(f"invalid input: {', '.join(invalid_inputs)}")
      
      
      negative_numbers = [number for number in integers_to_add if number < 0]

      if negative_numbers:
         raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
      return sum(integers_to_add)