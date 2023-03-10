import json

class register():
    __value = 0
    def __init__(self):
        pass   
    def reg_write(self,data):
        self.__value = data
    def reg_read(self):
        return self.__value



class machine():
    d_seg = 0x0000
    s_seg = 0x0050 #80 in decimal comment has to be deletde at the end
    e_seg = 0x0051 #81 in decimal comment has to be deletde at the end
    stackptr = 80 # changes while push
    __MC = [None] * 100
    __name__ = str
    __r1 = register()
    __r2 = register()
    __r3 = register()
    __generalpurpose =[__r1,__r2,__r3]
    def __init__(self,name):
        self.name = name

    def MC_write_data(self,addr,data):
        if addr < self.stackptr or addr > self.s_seg:
            self.__MC[addr] = data
        else:
            return None
            print("Data Overflow")

    def MC_read(self,addr):
        return self.__MC[addr]
    
    def MC_dump(self):
        return self.__MC
    
    def MC_clear(self):
        self.__MC = []

    def MC_Stack_push(self,data):
        self.__MC[self.stackptr] = data
        if self.stackptr > self.d_seg :
            self.stackptr -= 1
        else:
            print("Stack Overflow")

    def registerslct(self,reg):
        if reg == 1:
            return self.__r1
        elif reg == 2:
            return self.__r2
        elif reg == 3:
            return self.__r3
        else:
            return None
    def getregs(self):
        return self.__generalpurpose
    
    def retmachine(self):
        return {'MC': json.dumps(self.__MC), 'r1': self.__r1.reg_read(), 'r2': self.__r2.reg_read(), 'r3': self.__r3.reg_read() }
        


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

def machineoperation():
    cpu1 = machine("cpu1_machine")
    print(cpu1.name)
    buf =Buffer()
    buf.buffer_load("flag{cpu_hack_is_fun}")

    datain = buf.buffer_dump()
    print(datain)
    dataascii = []

    for i in datain:
        dataascii.append(hex(ord(i)))
    
    


    print(datain)
    print(dataascii)


    for i in range(21):
        if i < 7:
            cpu1.MC_Stack_push(dataascii[i])
        elif i < 14:
            cpu1.MC_write_data(i-7,dataascii[i])
        elif i < 18:
            cpu1.MC_write_data(i+67,dataascii[i])
        else:
            cpu1.registerslct(21-i).reg_write(dataascii[i])


    print(cpu1.MC_dump())


    for i in cpu1.getregs():
        print(i.reg_read())

    json.dump(cpu1.retmachine(),open("cpu1.json","w"))




machineoperation()