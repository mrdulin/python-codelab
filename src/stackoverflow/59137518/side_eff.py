class Handler:

    def is_connected(self):
        pass


class Backend:

    def initConnection(self):
        handlr = Handler()
        while(True):
            is_connected = handlr.is_connected()
            print(is_connected)
            if(is_connected):
                break
