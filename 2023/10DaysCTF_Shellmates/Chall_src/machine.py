class register():
    __value = 0
    def __init__(self):
        pass   
    def reg_write(self,data):
        self.__value = data



class machine():
    d_seg = 0x0000
    s_seg = 0x0050 #80 in decimal comment has to be deletde at the end
    stackptr = 80 # changes while push
    dataptr = 0 # changes while write in MC
    __MC = [None] * 100
    __name__ = str
    __r1 = register()
    __r2 = register()
    __r3 = register()

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

    def register_read(self,reg):
        if reg == 1:
            return self.__r1
        elif reg == 2:
            return self.__r2
        elif reg == 3:
            return self.__r3
        else:
            print("Wrong Register")


class Buffer:
    size = 21
    __buffer = [None] * size
    def __init__(self):
        pass
    def buffer_load(self,data):
        self.__buffer=list(data)
        self.__buffer=self.__buffer[:self.size]
    def buffer_dump(self):
        return self.__buffer





#flag{cpu_hack_is_fun} #21 char 


buf =Buffer()
buf.buffer_load("flag{cpu_hack_is_fun}")
print(buf.buffer_dump())



cpu1 = machine("cpu1_machine")
print(cpu1.name)

cpu1.MC_write_data(0,111)
cpu1.MC_write_data(1,222)
cpu1.MC_Stack_push(555)
cpu1.MC_Stack_push(666)
cpu1.MC_Stack_push("Amine")
cpu1.MC_Stack_push(888)
print(cpu1.MC_dump())


