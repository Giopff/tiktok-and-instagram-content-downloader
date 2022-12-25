from download import TDLALL
from sendT import sendTelmain

def launch():
    TDLALL()
    sendTelmain()

if __name__ == '__main__':
    launch()