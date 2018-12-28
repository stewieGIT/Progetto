from time import time
def timer(func):
    def wrapping_function(arg):
        start=time()
        value=func(arg)
        elapsed=time()-start
        file=open("result.txt", "a")
        space="------------------------"+str(func)+"\n"
        string="n:\t" + str(arg) + "\n"
        string2="t:\t" + str(elapsed) + "\n"
        file.write(space)
        file.write(string)
        file.write(string2)
        file.close()
        return value
    return wrapping_function

#applicare @timer sopra la funzione che voglio misurare
