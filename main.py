divid = int(input("Enter dividend integer"))
divi = int(input("Enter divisor integer"))

def divide(dividend, divisor):
    if divisor != 0:
        if dividend >= -2**31 and divisor <= (2**31)-1:



            quotient = dividend // divisor
            if quotient > (2**31)-1:
                return (2**31)-1
            elif quotient < -2**31:
                return -2**31
            else:
                return quotient
    elif ZeroDivisionError:
        print("Zero Division Error")

print(divide(divid,divi))
