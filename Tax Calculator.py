subTotal = float (input ('Enter amount: '))

salestaxPercent = 0.025

statetaxPercent = 0.05

StateTaxAmount = (subTotal * statetaxPercent)

SalesTaxAmount = (subTotal * salestaxPercent)

tax = (SalesTaxAmount + StateTaxAmount)

Total = (subTotal + tax)

print ( "Sub Total: $" + format( subTotal, ",.2f"), \
"Sales Tax: $" + format (StateTaxAmount, ",.2f"), \
"State Tax: $" + format (SalesTaxAmount, ",.2f"), \
"Total Tax Amount: $" + format (tax, ",.2f"), \
"Total: $" + format (Total, ",.2f") )

print ("Amanda Alcott-Herr")
#Chapter 2 ex 6 
#Create program that will calculate a total amount given by the user
#The program will then calculate the tax amount. 
# The user will be displayed with individual tax amounts and a total 
