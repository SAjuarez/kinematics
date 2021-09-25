import math

st_var = []

st_var.append(input("Enter value for vf: "))
st_var.append(input("Enter value for vi: "))
st_var.append(input("Enter value for a: "))
st_var.append(input("Enter value for d: "))
st_var.append(input("Enter value for t: "))

total = 0

for index, value in enumerate(st_var):
  
  if (any(char.isdigit() for char in value)):
    total = total + (2**index)
    
  if (value == "?"):
    total = total + 2**(10-index)
    st_var[index] = 10**2
    
    if (index == 1 or index == 2):
      w = " m/s"
    if (index == 2):  
      w = " m/s^2"
    if (index == 3):
      w = " m" 
    if (index == 4):
      w = " s" 

  if (value == "/"):
    st_var[index] = 10**2
    

vf = float(st_var[0])
vi = float(st_var[1])
a = float(st_var[2])
d = float(st_var[3])
t = float(st_var[4])

equations = {1046:vi+a*t, \
             275:(vf-vi)/t, \
             71:(vf-vi)/a, \
             150:(vi*t)+((a*(t**2))/2), \

             1038:math.sqrt((vi**2)+(2*a*d)), \
             267:((vf**2)-(vi**2))/(2*d), \
             135:((vf**2)-(vi**2))/(2*a), \
             282:(2*(d-(vi*t)))/(t**2), \

             1050:((2*d)/t)-vi, \
             147:((vf+vi)*t)/2, \
             75:(2*d)/(vf+vi), \
             78:((-vi)+math.sqrt(abs((vi**2)+2*a*d)))/a
}

print(str(equations.get(total)) + w)

if (total == 78):
  print(str((((-vi)-(math.sqrt(abs((vi**2)+2*a*d))))/a)) + w)
