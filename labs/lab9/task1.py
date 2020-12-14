class PrintAverage(Exception):
    pass

class PrintDisp(Exception):
    pass

class PrintAmount(Exception):
    pass


def so_coroutine():
    print("Starting coroutine")
    disp = 0
    averg = 0
    N = 0
    summ = 0
    simm_of_sqrt = 0
    try:
        while True:
            try:
                x = yield
                summ += x
                simm_of_sqrt += x**2
                N += 1
                averg = summ/N
                disp = simm_of_sqrt/N - averg**2
            except PrintAverage:
                yield averg
                
            except PrintDisp:
                yield disp
                
            except PrintAmount:
                yield N
    finally:
        print("So coroutine finished")
        
        
        
try:
    coroutine = so_coroutine()
    next(coroutine)
    coroutine.send(1)
    coroutine.send(5)
    coroutine.send(27)
    print('Average:', coroutine.throw(PrintAverage))
    next(coroutine)
    print('Dispersion:', coroutine.throw(PrintDisp))
    next(coroutine)
    coroutine.send(3)
    coroutine.send(17)
    coroutine.send(6)
    print('Amount:', coroutine.throw(PrintAmount))
    next(coroutine)
    print('Dispersion:', coroutine.throw(PrintDisp))
    next(coroutine)
    
except:
    pass
