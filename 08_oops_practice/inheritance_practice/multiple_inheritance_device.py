class Camera:
    def take_photo(self):
        return "Photo taken"
class Phone:
    def make_call(self, number):
        return f"Calling {number}"
class Smartphone(Camera, Phone):
    def browse_web(self, url):
        return f"Browsing {url}"
number_of_smartphones = int(input("Enter number of smartphones: "))
smartphones = []
for _ in range(number_of_smartphones):
    smartphone = Smartphone()
    smartphones.append(smartphone)
print(f"Smartphone: {smartphones}")
for idx, smartphone in enumerate(smartphones, start=1):
    print(f"Smartphone {idx}:")
    print(smartphone.take_photo())
    print(smartphone.make_call("123-456-7890"))
    print(smartphone.browse_web("www.example.com"))
