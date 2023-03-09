class machine():
    d_seg = 0x0000
    s_seg = 0x0050 #80 in decimal comment has to be deletde at the end
    stackptr = 0x0050 # changes while push
    __MC = list[100] 
    __name__ = str
    def __init__(self,name):
        self.name = name
    def MC_write_data(self,addr,data):
        self.__MC[addr] = data
    def MC_read(self,addr):
        return self.__MC[addr]
    def MC_dump(self):
        return self.__MC
    def MC_clear(self):
        self.__MC = list[100]
    def MC_Stack_push(self,data):
        self.__MC[self.stackptr] = data


cpu1 = machine("cpu1_machine")
print(cpu1.name)


