#!python

import random

def readopcodes(filename):
  with open(filename, 'r') as file:
    opcodes = []
    unclean = file.readline().split(sep=",")
    for digit in unclean:
      opcodes.append(int(digit))
    return opcodes


opcodes = readopcodes('input_2.txt')
noun = 0
verb = 0
while opcodes[0] != 19690720:
  opcodes = readopcodes('input_2.txt')
  noun = random.randint(0,99)
  verb = random.randint(0,99)

  opcodes[1] = noun
  opcodes[2] = verb

  for code in range(0, len(opcodes), 4):
    new_codes = opcodes[code:code+4]
    if new_codes[0] == 1:
      value = opcodes[new_codes[1]] + opcodes[new_codes[2]]
    if new_codes[0] == 2:
      value = opcodes[new_codes[1]] * opcodes[new_codes[2]]
    opcodes[new_codes[3]] = value
    new_codes = opcodes[code:code+4]
    if new_codes[0] == 99 or new_codes[3] == 99:
      break
  

print("Noun: " + str(noun))
print("Verb: " + str(verb))