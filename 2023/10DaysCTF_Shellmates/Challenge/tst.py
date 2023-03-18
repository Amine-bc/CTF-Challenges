
hex_str = '0xee'
hex_int = int(hex_str,16)
print(hex_int)   # Output: 238



def list_to_binary(lst):
    binary_str = ''.join(str(bit) for bit in lst)
    binary_int = int(binary_str, 2)
    return binary_int


print(bin(list_to_binary([1,0,1,1,1,0,1,0,0,1,1,1])))