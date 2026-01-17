with open("3ex.txt") as f:
    N = int(f.readline().strip())
    array = [int(f.readline().strip()) for i in range(N)]

array.sort()

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]


if N % 2 == 0:
    Q2 = (array[N // 2 - 1] + array[N // 2]) / 2
    lower_half = array[:N // 2]
    upper_half = array[N // 2:]
else:
    Q2 = array[N // 2]
    lower_half = array[:N // 2]
    upper_half = array[N // 2 + 1:]

Q1 = median(lower_half)
Q3 = median(upper_half)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

count = sum(1 for x in array if x < lower_bound or x > upper_bound)
print(count)