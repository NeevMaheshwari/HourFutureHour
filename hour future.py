hour=eval(input("Enter and hour between 1 and 12: "))
future=eval(input("Enter how many hours in future?: "))
newhour=hour+future
if newhour>12:
    nnhour=newhour-12
    print(nnhour,"o'clock")
else:
    print(newhour,"o'clock")



