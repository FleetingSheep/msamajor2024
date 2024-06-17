'''
flag = 1
for i in range(1, 100):
  for factor in range(2, (int((i / 2)) + 1)):
    if i % factor == 0: flag = 1
  if flag != 1: print(i, end=", ")
  flag = 0
'''

'''
dog_counter = 0
sentence = "I have a dog. My dog is cute. Do you want a dog?".rsplit(" ")
for i in sentence:
    if "dog" in i: dog_counter += 1
print(f"{dog_counter} dogs detected.")
'''
#OR

start_index = 0
dog_counter = 0
sentence = "I have a dog. My dog is cute. Do you want a dog?"
while True:
    start_index = sentence.find("dog", start_index) + 1
    if start_index == 0: break
    dog_counter += 1
print(f"{dog_counter} dogs detected.")