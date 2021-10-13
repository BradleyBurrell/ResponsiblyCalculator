import Functions

print("Hello and Welcome to V1 of the Responsibly Calculator")
amount = int(input("How much Responsibly, in ml, would you like to make?"))

porter_q = input('\tWould you like to include the Porter Coefficient? (y/n) ')
if porter_q.lower() == 'y':
    porter_a = True
if porter_q.lower() == 'n':
    porter_a = False
else:
    print("OI Cockwomble, read the question! I'll leave it up to Rando Cardrissian")
    porter_a = Functions.rando_cardrissian()
jonny_q = input('\tWould you like to include the Porter Coefficient? (y/n) ')
if jonny_q.lower() == 'y':
    jonny_a = True
if jonny_q.lower() == 'n':
    jonny_a = False
else:
    print("OI Cockwomble, read the question! I'll leave it up to Rando Cardrissian")
    jonny_a = Functions.rando_cardrissian()


Functions.responsibly_calculator(required_amount=amount,
                                 porter_coefficient=porter_a,
                                 the_jonnybrown_factor=jonny_a)