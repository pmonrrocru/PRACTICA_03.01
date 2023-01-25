import datetime

def fib_r(n):
    if n < 2:
        return n
    else:
        return fib_r(n - 1) + fib_r(n - 2)

start_time = datetime.datetime.now()
print(fib_r(1))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es de: ", end_time - start_time)






