print("Hello World!")
counties=["arapahoe", "denver", "jefferson"]



# if- else statements practice 
temperature= int(input("what is the temperature?"))

if temperature >80:
    print("turn AC on")
else:
    print("Open the windows")

#if- elif-else practice 
# What is the score?
score=int(input("What was your test score?"))

# Determine the grade.
if score >= 90:
    print("Your grade is an A")
elif score >= 80:
    print("Your grade is a B")
elif score >= 70:
    print("Your grade is a C")
elif score >= 60:
    print("you should study more lol")
else:
    print("L")


# practice Membership operators 

counties=["arapahoe", "denver", "jefferson"]

if "el paso" in counties:
    print("el paso is in counties list")
else:
    print("el paso is not cool enough to be on the list")

# practice both membership and logical operators 

counties=["arapahoe", "denver", "jefferson"]

if "arapahoe" in counties and "el paso" in counties:
    print("Both arapahoe and el paso on the cool guy list")
else:
    print("lol one of them is not cool enough, its prob el paso...")


if "arapahoe" in counties or "el paso" in counties:
    print("one of them is on the list, prob arapahoe")
else:
    print("arapahoe and el paso are not on the list")

# practice iterating thru lists and tuples

for county in [counties]:
    print(county)

