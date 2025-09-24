# accepted

cases = int(input())
results = []

for i in range(cases) :
    k,x = map(int, input().split(" "))
    x = (2**k)*x
    results.append(x)



for _ in results:
    print (_)