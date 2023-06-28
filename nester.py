from dos import print_lol

""" Nester main. Test cases """

my_europe_countries = ["Spain", "France", ["Italy", "Germany", ["England"]]]
my_asia_countries = ["Japan", ["China", ["Bhutan"], "India"], "Saudi-Arabia"]
my_america_countries = ["Canada", "Colombia", "Venezuela", ["Cuba", ["Chile", ["Argentina", ["El-Salvador"]]]]]

print_lol(my_europe_countries, 0, True)
print("")
print_lol(my_europe_countries, -2, True)
print("")
print_lol(my_asia_countries, 5, False)
print("")
print_lol(my_asia_countries, 5, True)
print("")
print_lol(my_america_countries, 2, True)
print("")
print_lol(my_america_countries, 2, False)
print("")
print_lol(my_america_countries)

