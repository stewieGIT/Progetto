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
        
        file = open("uf_results.txt", "a")
        space = f'------------------Function {func.__name__}------------------\n'
        string = "n:\t"+ str(args[2]) + "\n"
        string2 = "t:\t"+ str(elapsed) + "\n\n"
        file.write(space)
        file.write(string)
        file.write(string2)
        file.close()
        
        print(f'Function {func.__name__} with n = {args[2]} took {elapsed} seconds')
        return value
    return wrapping_function


def timerDFS(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)               # chiamata alla funzione da decorare
        elapsed = time() - start
        
        file = open("dfs_results.txt", "a")
        space = f'-------------Function {func.__name__}-------------\n(partendo dal nodo {args[1]})\n'
        string = "n:\t"+ str(args[2]) + "\n"
        string2 = "t:\t"+ str(elapsed) + "\n\n"
        file.write(space)
        file.write(string)
        file.write(string2)
        file.close()
        
        print(f'Function {func.__name__} with n = {args[2]} took {elapsed} seconds')
        return value
    return wrapping_function
#applicare @timer sopra la funzione che voglio misurare