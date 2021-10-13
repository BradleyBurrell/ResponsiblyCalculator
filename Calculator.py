import random


def responsibly_calculator(required_amount, porter_coefficient, the_jonnybrown_factor):

    # The Boob Ratio
    pimm = 2
    gin = 1
    jager = 1
    fruit_cider = 20

    # The Shirra Formula
    parts = required_amount / (pimm + gin + jager + fruit_cider)
    ml_pimms = int(parts * pimm)
    ml_gin = int(parts * gin)
    ml_jager = int(parts * jager)

    if porter_coefficient is True:
        ml_pimms = int(ml_pimms * random.randint(-2, 2))
        if ml_pimms == 0:
            ml_pimms = 2
        elif ml_pimms < 0:
            ml_pimms = int(ml_pimms * -1)
        ml_gin = int(ml_gin * random.randint(-2, 2))
        if ml_gin == 0:
            ml_gin = 2
        elif ml_gin < 0:
            ml_gin = int(ml_gin * -1)
        ml_jager = int(ml_jager * random.randint(-2, 2))
        if ml_jager == 0:
            ml_jager = 2
        elif ml_jager < 0:
            ml_jager = int(ml_jager * -1)

    if the_jonnybrown_factor is True:
        ml_pimms = int(ml_pimms * random.uniform(1, 2))
        ml_gin = int(ml_pimms * random.uniform(1, 2))
        ml_jager = int(ml_pimms * random.uniform(1, 2))

    spirt_sum = ml_pimms + ml_gin + ml_jager

    ml_fruit_cider = required_amount - spirt_sum

    total = ml_pimms + ml_gin + ml_jager + ml_fruit_cider
    print("""
{0}
Pimms      : {1}ml
Gin        : {2}ml
Jager      : {3}m
Fruit Cider: {4}ml
{5}
Total: {6}ml
{0}""".format("="*40, ml_pimms, ml_gin ,ml_jager, ml_fruit_cider, '-' * 40, total))


def rando_cardrissian():
    return random.choice([True, False])

print("Hello and Welcome to V1 of the Responsibly Calculator")
amount = int(input("How much Responsibly, in ml, would you like to make?"))

porter_q = input('\tWould you like to include the Porter Coefficient? (y/n) ')
if porter_q.lower() == 'y':
    porter_a = True
if porter_q.lower() == 'n':
    porter_a = False
else:
    print("OI Cockwomble, read the question! I'll leave it up to Rando Cardrissian")
    porter_a = rando_cardrissian()
jonny_q = input('\tWould you like to include the Porter Coefficient? (y/n) ')
if jonny_q.lower() == 'y':
    jonny_a = True
if jonny_q.lower() == 'n':
    jonny_a = False
else:
    print("OI Cockwomble, read the question! I'll leave it up to Rando Cardrissian")
    jonny_a = rando_cardrissian()

if __name__ == '__main__':
    responsibly_calculator(required_amount=amount,
                           porter_coefficient=porter_a,
                           the_jonnybrown_factor=jonny_a)
