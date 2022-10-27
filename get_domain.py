"""A simple program that extract the domain name"""

def get_website_domain(website):

    domain=website.split(".")[1]
    return domain

print(get_website_domain("www.cnn.com"))
print(get_website_domain("www.umd.edu"))
print(get_website_domain("www.youtube.com")) 
