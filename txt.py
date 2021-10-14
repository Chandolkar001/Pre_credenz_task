import re
# import socket
text_t = '''
12 34
345 56 5 67 
192.168.0.1
366.1.2.2
345
'2002-01-01'
'shreyas' 2003 'hhii' 678 djfnjn 3
fghrufh '45' jnjnrjkg789 iunidfngi 345 2003-12-27
'''

# ips = '110.234.52.124'
# main components.
# r'\d{3,}'
# r'(19|20)\d\d[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])' also \d{4}[-]\d{2}[-]\d{2}
# r"(['])([\w]+)(['])" group(2)
# IP address
# r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
# ips = input 
# mess = pattern.finditer(ips)
# message = bool(pattern.findall(ips))
# if message == False:
#     print("Invalid")
# else:
#     for m in mess:
#         pick = int(m.group(2))
#         if pick > 0 and pick < 127:
#             print("Valid Class A")
#         elif pick >= 128 and pick <= 191:
#             print("Valid Class B")
#         elif pick >= 192 and pick <= 223:
#             print("Valid Class C")
# mac address
# ret_text = "01-23-45-67-89-AB"
# pattern = re.compile(r"^([0-9A-Fa-f]{2}[:-])" +"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
# message = pattern.finditer(ret_text)
# for m in message:
#     print(m)


# def snake(match):
#     return match.group(1).lower() + "_" + match.group(2).lower()

words = """MyClass
MyClassFactory
MyClassFactoryBuilder
MyClassFactoryBuilderImpl
myInstance
myInstance2
abc
patternMatcher""".splitlines()

# results = [re.sub(r"(.+?)([A-Z])", snake, w, 0) for w in words]

# for m in results:
#     print(m)
 

def extract_num(userinput):
    pattern = re.compile(r'\d{3,}')
    matches = pattern.findall(userinput)
    return matches

def extract_date(userinput):
    pattern = re.compile(r'(19|20[0-9][0-9])[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])')
    matches = pattern.findall(userinput)
    return matches

def extract_quote(userinput):
    initlist = []
    pattern = re.compile(r"(['])([a-zA-Z0-9_.+-]+)(['])")
    matches = pattern.finditer(userinput)
    for m in matches:
        x = m.group(2)
        initlist.append(x)
    return initlist

def IPvalidatar(userinput):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
    mess = pattern.finditer(userinput)
    message = bool(pattern.findall(userinput))
    if message == False:
        result = 0
    else:
        for m in mess:
            pick = int(m.group(2))
            if pick > 0 and pick < 127:
                result = 1
            elif pick >= 128 and pick <= 191:
                result = 2
            elif pick >= 192 and pick <= 223:
                result = 3
    
    return result 

def MACvalidatar(userinput):
    pattern = re.compile(r"^([0-9A-Fa-f]{2}[:-])" +"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
    message = bool(pattern.findall(userinput))
    if message == True:
        result = 1
    else:
        result = 2
    return result

def Cam_to_Sna(userinput):
    def snake(match):
        return match.group(1).lower() + "_" + match.group(2).lower()
    
    result = [re.sub(r"(.+?)([A-Z])", snake, w, 0) for w in userinput]
    return result

demt = 'camelCase'
results = Cam_to_Sna(words)
print(results)
