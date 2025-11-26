num = "52"

# Converting string to integer for easy calculations
int_num = int(num)

curr_max = -1
if(int_num % 2!= 0):
    curr_max = int_num
while(int_num > 0):
    lastDigit = int_num % 10
    int_num = int_num//10
    if (lastDigit%2!=0 ):
        curr_max = lastDigit
    elif(int_num % 2 != 0):
        curr_max = int_num
        break
print("Maximum ODD in the number is : " , curr_max)