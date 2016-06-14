def prime_number(n):
    primenumber = [2]
    init_val = 3
    for item in range(3, n):
        if item % 2 !=0:
            primenumber.append(item)
            init_val +=1     
    return primenumber
print prime_number(290)
