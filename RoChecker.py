import string, random, time
from requests_html import HTMLSession

chars = string.ascii_letters
session = HTMLSession()

while True:
    randomnum = random.randint(3,5)
    name = ''.join(random.choice(chars) for i in range(randomnum))
    r = session.get(f'https://www.roblox.com/UserCheck/doesusernameexist?username={name}')
    if r.html.search('True'):
        print(name, "NOT AVAILABLE")
    else:
        print(name, "AVAILABLE")
        file = open("names.txt","a")
        file.write(name + " is available " + "\n")
        file.close()
    time.sleep(0.2)


