class Numbers:
    def even():
        print("EVEN NUMBERS")
        a=int(input("Enter a starting rang -> "))
        b=int(input("Enter a ending range -> "))
        for x in range (a,b+1):
            if x%2==0:
                print(x,end=" ")
    def odd():
        print("ODD NUMBERS")
        a=int(input("Enter a starting rang -> "))
        b=int(input("Enter a ending range -> "))
        for y in range (a,b+1):
            if y%2!=0:
                print(y,end=" ")
obj=Numbers
obj.even()
print("\n")
obj.odd()
