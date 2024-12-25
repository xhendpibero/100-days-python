# QUESTION NO 3:
file = open("my text file.py.txt", "w")
file.write('subhanshawat\nlovely professional university')
file.close()

file = open("my text file.py.txt", "r")
content = file.read()
character_count = len(content)
print(character_count)
file.close()