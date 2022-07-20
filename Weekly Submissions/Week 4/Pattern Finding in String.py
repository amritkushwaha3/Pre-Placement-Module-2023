n=int(input("Enter number of cities : "))

city=()

for i in range(n):
    c=input("Enter City : ")
    city+=(c,)

print(city)

pat=input("Enter Pattern you want to search for? ")

for c in city:
    if(c.find(pat)!=-1):
        print(c)
