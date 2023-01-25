import datetime

def fib_i(n):
    if n == 0 or n == 1:
        return n

    ant2 = 0
    ant1 = 1
    for i in range(2, n+1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn

start_time = datetime.datetime.now()
print(fib_i(40))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es de: ", end_time - start_time)







