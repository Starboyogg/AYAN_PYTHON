class Array:
    def main_array():
        arr_1=[]
        n=int(input("Enter the no of array element"))
        for x in range(0,n): #starts from 0 upto 4 if n=5
            ele=int(input())
            arr_1.append(ele)
        print("ORIGINAL ARRAY-> ",arr_1)
        print(type(arr_1))
        arr_1.sort()
        print("ASCENDING ORDER->",arr_1)
        arr_1.sort(reverse=True)
        print("DESCENDING ORDER->",arr_1)
object=Array
object.main_array()




