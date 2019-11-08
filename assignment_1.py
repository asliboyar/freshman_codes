'''
Write a program to create a customer’s bill for a company. The company sells only five assorted products: TV, DVD Player, Game Controller, Game Console, and Cell Phone. The program must read the unit prices for each of the products from the keyboard. The program must read the quantity of each piece of equipment purchased from the keyboard. It then calculates the cost of each item, the subtotal, and the total cost after an 8.25% sales tax.
The input data consists of a set of floating point numbers representing the unit price for each of the products. The input data consist of a set of integers representing the quantities of each item sold. All inputs must be captured into the program in a user-friendly way; that is, the program must prompt the user for each quantity as shown below. The numbers in boldface show the user’s answers.
'''

tv_p=float(input("What is the unit price of a TV? "))
tv_q=int(input("How Many TVs Were Sold? "))
dvd_p=float(input("What is the unit price of a DVD player? "))
dvd_q=int(input("How Many DVD Players Were Sold? "))
gcontroller_p=float(input("What is the unit price of a Game Controller? "))
gcontroller_q=int(input("How Many Game Controllers Were Sold? "))
gconsole_p=float(input("What is the unit price of a Game Console? "))
gconsole_q=int(input("How Many Game Consoles Were Sold? "))
cellphone_p=float(input("What is the unit price of a Cell Phone? "))
cellphone_q=int(input("How Many Cell Phones Were Sold? "))

print("_"*60)
print("QTY\t\tDESCRIPTION\t\t\t\tUNIT PRICE\t\tTOTAL PRICE ")
print('-'*60)

print(tv_q, "%10s" % "TV", "%28s" % tv_p, "%15s" %  float(tv_p*tv_q))
print(dvd_q, "%18s" % "DVD Player", "%20s" % dvd_p, "%15s" % float(dvd_p*dvd_q))
print(gcontroller_q, "%23s" % "Game Controller","%15s"% gcontroller_p,  "%15s" % float(gcontroller_p*gcontroller_q))
print(gconsole_q, "%20s" % "Game Console","%18s"% gconsole_p,  "%15s" % float(gconsole_p*gconsole_q))
print(cellphone_q, "%18s" % "Cell Phone","%20s"% cellphone_p,  "%15s" % float(cellphone_p*cellphone_q))
print("%60s"%"---------------")

subtotal=float((tv_p*tv_q) + (dvd_p*dvd_q) + (gcontroller_p*gcontroller_q) + (gconsole_p*gconsole_q) + (cellphone_p*cellphone_q))
tax=float((8.25*subtotal)/100)
print("                               SUBTOTAL              ", subtotal)
print("                               TAX                   ", tax)
print("                               TOTAL                 ", tax+subtotal)
