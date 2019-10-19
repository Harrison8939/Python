#Declaring constant values
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#declaring starting values of temps
c_temp = 0
f_temp = 0

#converts fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

#converts celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)
  return f_temp

c0_in_fahrenheit = c_to_f(0)

#calculates force from mass * acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass,train_acceleration)


#calculates energy from mass times the speed of light squared
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

#calculates force multiplied by distance to give total work
def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)




#tests


print ("100 degrees fahrenheit is " + str(f100_in_celsius) + " celsius")


print("0 degrees celsius is " + str(c0_in_fahrenheit) + " Fahrenheit")

print ("The GE train supplies", train_force,"Newtons of force.")

print("A 1kg bomb supplies "+str(bomb_energy)+" Joules")

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
