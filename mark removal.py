import re
text = "douleuei! ta thaumastika aferountai! odws!"
updated = re.sub(r'!+(?!!*$)','', text)
print (updated)