# Write your solution here
def factorials(n: int):
    
    numbers={}
    j=1
    for i in range(1, n+1):
        numbers[i] = i*j
        j=numbers[i]
    return numbers    


if __name__=="__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])