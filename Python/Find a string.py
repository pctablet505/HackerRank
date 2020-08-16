def count_substring(string, sub_string):
    count=0
    i=0    
    while True:
        if string.find(sub_string,i)<0:
            break
        
        elif string.find(sub_string,i)>=0:
            s=string.find(sub_string,i)
            i=s+1
            count+=1
    return count



