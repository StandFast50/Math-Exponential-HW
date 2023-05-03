#intital amount
a = 
# rate
r = 
# makes the rate turn into a decimal if a fraction
r = r/100
# time
t = 
#number of times compounded yearly
n = 0
# keep n 0 if it's not 3 or 4
compound = input("1. Growth, 2. Decay, 3. total, 4. interest: ")

if compound == "1":
    compound = (a*(1 + r)**t)
elif compound == "2":
   compound = (a*(1 - r)**t)
elif compound == "3":
    compound =(a*(1 + (r/n))**(n*t))
elif compound == "4":
    compound =(a*(1 + (r/n))**(n*t)) - a
print(round(compound,2))
