def print_formatted(number):
    l=len('{0:b}'.format(number))
    for i in range(1,number+1):
        print('{}'.format(i).rjust(l),'{0:o}'.format(i).rjust(l),'{0:X}'.format(i).rjust(l),'{0:b}'.format(i).rjust(l),sep=' ')
    # your code goes here

