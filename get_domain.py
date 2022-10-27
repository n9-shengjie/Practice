"""A simple program that extract the domain name"""

from distutils.util import split_quoted


def get_website_domain(website):

    domain=website.split(".")[1]
    return domain

print(get_website_domain("www.cnn.com"))
print(get_website_domain("www.umd.edu"))
print(get_website_domain("www.youtube.com")) 

def split_check(customer_name, total_check, fraction_owed):
    amount_owed = round(total_check * fraction_owed, 2)
    return customer_name + ' owes ' + str(amount_owed)
    raise NotImplementedError

test_name = "Kev"
test_check = 100
test_fraction = 0.25
print(split_check(test_name, test_check, test_fraction))