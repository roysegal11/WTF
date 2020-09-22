import sys
import time

if __name__ == "__main__":
    numb = int(sys.argv[1])+1
    for i in range(numb):
        if i != 0:
            print(str(i)+" "+str(i*i))
            time.sleep(1)
