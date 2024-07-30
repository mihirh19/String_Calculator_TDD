import re
class string_calculator:
   def add(self, numbers : str) -> int:
      if not numbers:
         return 0
      delimiter = ','

      if numbers.startswith("//"):
         delimiter, numbers = numbers[2:].split("\n", 1)

      numbers = numbers.replace('\n', delimiter)
      integers_to_add= re.split(re.escape(delimiter), numbers)
      integers_to_add= list(map(int, integers_to_add))

      return sum(integers_to_add)