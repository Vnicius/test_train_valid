import sys

fl = open(sys.argv[1], "r")
lang = sys.argv[2]
lines = fl.readlines()
train = open("train." + lang, "w")
test = open("test." + lang, "w")
valid = open("valid." + lang, "w")

for l in lines[:int(len(lines) * 0.88)]:
	train.write(l)

for l in lines[int(len(lines) * 0.88): int(len(lines) * 0.9)]:
	test.write(l)	

for l in lines[int(len(lines) * 0.9): len(lines)]:
	valid.write(l)
