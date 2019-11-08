'''
Write a python program with appropriate comments that creates customers’ bills for a carpet company when given the following information:
The length and the width of the carpet in feet
The carpet price per square foot
The per cent discount for each customer
The labor cost is fixed at $0.35 per square foot and is to be defined as a constant. 
The tax rate is 8.5% applied after the discount. It is also to be defined as a constant.
The input data consist of a set of three integers representing the length and width of the room to be carpeted, the percentage of the discount the owner gives to a customer, and a real number representing the unit price of the carpet. The program is to prompt the user for this input as shown below.
'''
'''
length=l
width=l
discount=d
cost per square foot=cpsf
'''
area=0
tax_rate=8.5/100


#This function is used to read all data and place them in the variables
def inputs_data():
  global l
  global w
  global d
  global cpsf
  l=int(input("Length of room (feet)? " ))
  w=int(input("Width of room (feet)? "))
  d=int(input("Customer discount(percent)? "))
  cpsf=float(input("Cost per square foot? "))
#This function calculates area, carpet cost, labor cost, and installed price. The installed price is the cost of the carpet and the cost of the labor.

def installed_price(l, w, cpsf):
  global carpet_cost
  global labor_cost
  global installed_price
  area=l*w
  carpet_cost=(area*cpsf)
  labor_cost=0.35*cpsf
  installed_price=carpet_cost+labor_cost

#This function calculates the discount and subtotal.
def subtotal(installed_price, d):
  global subtotal
  subtotal=installed_price-(d/100)

#This function calculates the tax and the total price.
def total(subtotal):
  global total
  global tax
  tax=tax_rate*subtotal
  total=subtotal+tax_rate*subtotal

def measurements(l, w, area):
  print("\t\tMEASUREMENTS\t\t")
  print("Length", 4*'\t', l,"ft.")
  print("Width", 4*'\t', w,"ft.")
  print("Area", 4*'\t', area, "square ft.")

def charges(cspf, carpet_cost, labor_cost, d):
  print ("\n\n")
  print("\t\t\t\t\tCHARGES\t\t\t\t\t")
  print("DESCRIPTION",'\t\t\t', "COST/SQUARE FT", '\t\t', "CHARGE")
  print('___________________________________________________________')
  print('Carpet', 6*'\t', cpsf, 5*'\t', "$",carpet_cost)
  print('Labor', 6*'\t', "0.35", 5*'\t  ',labor_cost)
  print('                                               ____________')
  print('INSTALLED PRICE', 9*'\t', "$", installed_price)
  print('Discount', 5*'\t', d, "%", 5*'\t  ', d/100*installed_price)
  print('                                               ____________')
  print('SUBTOTAL', 11*'\t', "$", subtotal)
  print('Tax', 12*'\t  ',tax)
  print('TOTAL', 12*'\t', "$", total)
 

inputs_data()
installed_price(l,w,cpsf)
subtotal(installed_price, d)
total(subtotal)
measurements(l, w, area)
charges(cpsf, carpet_cost, labor_cost, d)
