#This will solve kinematic problems given 3 var and solving for 1

st_var = []

st_var.append(input("Enter value for vf: "))
st_var.append(input("Enter value for vi: "))
st_var.append(input("Enter value for a: "))
st_var.append(input("Enter value for d: "))
st_var.append(input("Enter value for t: "))

total = 0

for index, val in enumerate(st_var):
  if (val.isnumeric()):
    total += 2**index
  if (val == "?"):
    total += 2**(10-index)

if (total)