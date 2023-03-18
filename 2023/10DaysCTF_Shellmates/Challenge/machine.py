import json, random

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
    __r4 = register()
    __generalpurpose =[__r1,__r2,__r3]
    def __init__(self,name):
        self.name = name
        self.__MC = [hex(random.randint(0,100)) for i in range(100)]

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
    def setr4(self,data):
        self.__r4.reg_write(data)
    
    def retmachine(self):
        return {'name': 'flagmachine','MC': json.dumps(self.__MC), 'r1': self.__r1.reg_read(), 'r2': self.__r2.reg_read(), 'r3': self.__r3.reg_read(), 'r4': self.__r4.reg_read() }
        


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



def codingfunc(chars):
    # Initialize the MSB list with zeros
    msb = [0] * len(chars)

    # Convert each character to its integer value and shift it
    for i, char in enumerate(chars):
        shifted_value = int(char,16) >> 1
        msb[i] = (int(char,16) & 1)  # Extract the MSB before shift
        chars[i] = hex(shifted_value)

    # Return the shifted chars and MSB as a tuple
    return msb, chars


def list_to_binary(lst):
    binary_str = ''.join(str(bit) for bit in lst)
    binary_int = int(binary_str, 2)
    return binary_int


#flag{cpu_hack_is_fun} #21 char 

def machineoperation():
    cpu1 = machine("cpu1_machine")
    print(cpu1.name)
    buf =Buffer()
    buf.buffer_load("flag{5pu_h4ck_1es_F4n}")

    datain = buf.buffer_dump()
    print(datain)
    dataascii = []

    for i in datain:
        dataascii.append(hex(ord(i)))
        

    print(datain)
    print(dataascii)

    f8b = dataascii[0:8]
    lsb, f8b = codingfunc(f8b)
    #print(f8b)
    #print(lsb)
    lsb = list_to_binary(lsb)
    lsb = hex(lsb)
    cpu1.setr4(lsb)

    for i in range(21):
        if i < 7:
            cpu1.MC_Stack_push(f8b[i])
        elif i < 14:
            cpu1.MC_write_data(i-7,dataascii[i])
        elif i < 18:
            cpu1.MC_write_data(i+67,dataascii[i])
        else:
            cpu1.registerslct(21-i).reg_write(dataascii[i])


    #print(cpu1.MC_dump())


    for i in cpu1.getregs():
        print(i.reg_read())

    json.dump(cpu1.retmachine(),open("Challenge/flagmachine.json","w"))




machineoperation()