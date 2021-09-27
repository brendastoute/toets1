print ("welkom bij de auditie")
geelen = 4
mevrouwwit= 20
groenwoud = 30
var1= 0
var2= 0 
var3= 0

zin = input("wilt u aanmelden voor een rol?\nja,nee\n")
if zin == "ja":

    leeftijd = int(input("hoe oud is u?\n"))
    diploma = input("heeft u een diploma\nja,nee\n")
    gender = input("bent u een man of een vrouw?\n")
    verlegen = input("bent u verlegen?\nja,nee\n") 
    boos = input("word u snel boos?\nja,nee\n")

    if leeftijd >= 18:
        var1 = var1 + 1

    elif leeftijd <=18:
        var2 = var2 + 4

    elif leeftijd >= 20:
        var3 = var3 + 3


    if diploma == "ja":
        var1 = var1 + 0

    if diploma == "nee": 
        var2 = var2 + 2
        var3 = var3 + 9

    if gender == "man":
        var2 = var2 + 3
        var1 = var1 + 0

    if gender == "vrouw":
        var3 = var3 + 2

    if verlegen == "ja":
        var1 = var1 + 2
        var2 = var2 + 7

    elif verlegen == "nee":
        var3 = var3 + 0

    if boos =="ja":
        var3 == var3 + 15
    elif boos == "nee":
        var2 = var2 + 4
        var1 = var1 + 1


    if geelen > var1 or geelen <=4 :
        print ("u hebt te rol van geelen")

    elif mevrouwwit > var2 or mevrouwwit <= 20:
        print("u hebt de rol van mevrouw de wit")

    elif groenwoud > var3 or groenwoud <= 30:
        print("u heeft de rol van groenwoud")


elif zin == "nee":
    print("uhm ok?")


print(var1)
print(var2)
print(var3)


