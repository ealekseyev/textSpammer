import keyboard
from time import sleep
from sys import argv

print("Starting in...")
for i in range(6)[1::][::-1]:
	print(i)
	sleep(1)

with open(argv[1], "r") as f:
	words = f.read().replace("\n", " ")
	words = words.split(" ")

for word in words:
	keyboard.write(word + "\n")
	sleep(float(argv[2]))
