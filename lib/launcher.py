from download import TDLALL
from download import IDLALL
from sendT import sendTelmain



def launch():
    IDLALL()
    TDLALL()
    #sendTelmain()

if __name__ == '__main__':
    launch()
