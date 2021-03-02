
a = [[4,8],[2,5],[17,20],[10,21],[9,18]]

def maxFlights_kadane(a):
    k_arr = [0] * 24
    sum = 0
    max_flight=0
    for i in range(len(a)):
        k_arr[a[i][0]] += 1
        k_arr[a[i][1]] += -1

    for i in range(len(k_arr)):
        sum += k_arr[i]
        max_flight = max(sum, max_flight)
        if sum < 0:
            sum = 0

    print(f"Maximum flights in air at a time: {max_flight}")


maxFlights_kadane(a)





