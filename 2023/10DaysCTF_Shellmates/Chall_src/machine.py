class machine():
    d_seg = 0x0000
    s_seg = 0x0050 #80 in decimal comment has to be deletde at the end
    stackptr = 80 # changes while push
    dataptr = 0 # changes while write in MC
    __MC = [None] * 100
    __name__ = str
    def __init__(self,name):
        self.name = name

    def MC_write_data(self,addr,data):
        self.__MC[addr] = data
        self.__MC[self.stackptr] = data
        if self.dataptr  < self.stackptr - 1:
            self.stackptr += 1
        else:
            print("Data Overflow")

    def MC_read(self,addr):
        return self.__MC[addr]
    
    def MC_dump(self):
        return self.__MC
    
    def MC_clear(self):
        self.__MC = []

    def MC_Stack_push(self,data):
        self.__MC[self.stackptr] = data
        if self.stackptr > self.dataptr + 1:
            self.stackptr -= 1
        else:
            print("Stack Overflow")


cpu1 = machine("cpu1_machine")
print(cpu1.name)

cpu1.MC_write_data(0,111)
cpu1.MC_write_data(1,222)
cpu1.MC_Stack_push(555)
cpu1.MC_Stack_push(666)
cpu1.MC_Stack_push("Amine")
cpu1.MC_Stack_push(888)
print(cpu1.MC_dump())


