#check if the array consists two numbers which sums to 8


#a = [0, 0,1,1,1,1, 4, 6, 5, 9]
a = [0, 0,1,1,1,1, 4, 6, 7, 9]

def find_sum_iterative(a):
    no_iter=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            no_iter += 1
            if a[i] + a[j] == 8:
                print(f"No. of iterations {no_iter}")
                return True
    print(f"No. of iterations {no_iter}")
    return False

b = []
def find_sum_diff(a):
    no_iter = 0
    for i in range(len(a)):
        no_iter += 1
        if a[i] in b:
            print(f"No. of iterations {no_iter}")
            return True
        elif a[i] > 8:
            print(f"No. of iterations {no_iter}")
            return False
        else:
            b.append(8-a[i])
    print(f"No. of iterations {no_iter}")
    return False

print(find_sum_iterative(a))
print(find_sum_diff(a))
A=10

