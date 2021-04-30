
def change_making(d, n): 
    # your code goes here:
    result = []
    for i in range(len(d)-1, -1, -1):
        #find largest number in array
        largest = -1
        for num in d:
            if num > largest:
                largest = num
        #n - largest number until we can't anymore
        while(n >= largest):
            n-=largest
            result.append(largest)
        #find largest in d and remove it
        for i in range(len(d)):
            if d[i] == largest:
                d[i] = -1
        
    print(result)


if __name__ == "__main__":
    d = [1,2,3]
    n = 10
    e = [1,5,3]
    m = 14
    print(change_making(d,n))
    print(change_making(e,m))
