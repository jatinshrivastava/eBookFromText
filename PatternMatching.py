import re
text = "﻿[14/08/18, 7:50:51 PM] Aashish: Good intentions without actions, is like Soul without body, However pure it is, it can not bring any difference"  
result = re.sub(r'(([ [ ]\d\d/\d\d/\d\d, [0-1]?[0-9])|([2][0-3])):([0-5]?[0-9])(:([0-5]?[0-9] [AP]M[]] [a-zA-Z]*[:]))?', "", text)  
print(result)  
