# firstly need to know what is difference between signed and unsigned intigers
# unsigned is form <0;4294967295>
# signed is from <-2147483648;2147483647>

# function increase number by 2147483648, so if we give -2147483648 it's equal to 0
def signed_integer_to_unsigned_integer(intiger):
    return intiger+2**31

#function check digit if it is 32-bits int it return it back, otherwise return 0
def is_Unsigned_int32(intiger):
    if not(signed_integer_to_unsigned_integer(intiger) >> 32):
        return intiger
    else:
        return 0

#i used reverse of strings to reverse the digit,
# if it's negative digit it took "-" reverse string (number) without sign (which is '-') and glue these two values together at the end
#else it just reverse
#at the end return int value
def reverse_digit_32_bit(val):
    x = str(is_Unsigned_int32(val))
    if x[0] == '-':
        a = x[::-1]
        rev=x[0]+a[:-1]
    else:
        rev=x[::-1]

    return int(rev)

if __name__ == "__main__":
    val = int(input())
    reverse_digit_32_bit(val)
