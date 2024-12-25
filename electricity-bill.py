def energy_charges(unit_consumed):
  if(0<unit_consumed<=50):
    cost_per_unit=2.00
  elif(51<=unit_consumed<=100):
    cost_per_unit=2.50
  elif(101<=unit_consumed<=150):
    cost_per_unit=2.75
  elif(151<=unit_consumed<=250):
    cost_per_unit=5.25
  elif(251<=unit_consumed<=500):
    cost_per_unit=6.30
  elif(501<=unit_consumed<=800):
    cost_per_unit=7.10
  elif(801<=unit_consumed):
    cost_per_unit=7.52
  else:
    print("Invalid input.")
  return cost_per_unit

unit_consumed=float(input("Enter units:"))
cost_per_unit=energy_charges(unit_consumed)
fixed_charges=float(input("Enter fixed charges:"))

total_bill=(unit_consumed*cost_per_unit)+fixed_charges
print("The electricity bill of the month:",total_bill)