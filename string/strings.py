s = 'my name is Niteen'

print(s)  # my name is Niteen
print(len(s))  # 17
print('Niteen' in s)  # True
print('Niteen1' in s)  # False
print('Niteen1' not in s)  # True
print(s.find('name'))  # 3
print('#'.join(s))  # m#y# #n#a#m#e# #i#s# #N#i#t#e#e#n

s = '''my   
    name is 
    Niteen'''
print(s)  # print in multiline same as above
