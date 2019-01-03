from time import time


def timer(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)               # chiamata alla funzione da decorare
        elapsed = time() - start
        
        file = open("dati.txt", "a")
        space = "--------------------------\n"
        string = "n:\t"+ str(args[2]) + "\n"
        string2 = "t:\t"+ str(elapsed) + "\n"
        file.write(space)
        file.write(string)
        file.write(string2)
        file.close()
        
        print(f'Function {func.__name__} with n = {args[2]} took {elapsed} seconds')
        return value
    return wrapping_function

