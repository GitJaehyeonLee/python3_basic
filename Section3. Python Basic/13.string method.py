s = "My name is Mike."

print(s)

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("###############")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))