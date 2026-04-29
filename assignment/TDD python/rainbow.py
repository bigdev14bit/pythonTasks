import random

print("*** Random Rainbow Generator ***")

for i in range(1, 11):
  color_num = random.randint(1, 7)

  if color_num == 1:
    color = "Red"
  elif color_num == 2:
    color = "Orange"
  elif color_num == 3:
    color = "Yellow"
  elif color_num == 4:
    color = "Green"
  elif color_num == 5:
    color = "Blue"
  elif color_num == 6:
    color = "Indigo"
  else:
    color = "Violet"
print(color)
