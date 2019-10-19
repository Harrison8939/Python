#defines a function, calculating the age, with two parameters, returns age of person with a calculation
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049,1993)
dads_age = calculate_age(2049,1953)

print("I am",my_age,"Years old","and my dad is",dads_age,"Years old")