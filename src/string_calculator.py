import re
class string_calculator:
   def add(self, numbers : str) -> int:
      if not numbers:
         return 0
      
      integers_to_add= re.split(r',|\n', numbers)
      integers_to_add= list(map(int, integers_to_add))

      return sum(integers_to_add)