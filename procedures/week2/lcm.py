def lcm(a,b):
  if (a > b):
      maximum = a
  else:
      maximum = b
  while (True):
      if (maximum % a == 0 and maximum % b == 0):
          break
      maximum = maximum + 1
  return maximum

def lcm_run():
  print("The LCM of 47, 13 is", lcm(47,13))
  print("The LCM of 78, 25 is",lcm(78,25))