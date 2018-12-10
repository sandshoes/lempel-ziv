import time
t0 = time.time()
t = 0
alphabet = {}
text = ''
file = open('compression.txt','rb')
f = open('decompressed.txt','w', encoding = 'latin-1')

def retrace(pos,value, bit_string):
	p = pos-1
	string = bit_string[27*p+19:27*(p+1)].encode('latin-1')
	string = chr(int(string, 2))
	string += value
	up = bit_string[27*p:27*p+19]
	up = int(up,2)
	if up != 0:
		return retrace(up,string,bit_string)
	else:
		return string


bit_string = ""
byte = file.read(1)
while(len(byte) > 0):
	byte = ord(byte)
	bits = bin(byte)[2:].rjust(8, '0')
	bit_string += bits
	byte = file.read(1)
padded_info = bit_string[:8]
extra_padding = int(padded_info, 2)

bit_string = bit_string[8:] 
bit_string = bit_string[:-1*extra_padding]
for i in range(0,len(bit_string),27):
	char = bit_string[i:27+i]
	bin_pos = char[:19]
	pos = int(bin_pos,2)

	value = char[19:27].encode('latin-1')
	alphabet[char] = chr(int(value, 2))
	value = alphabet[char]
	if pos != 0:
		string = retrace(pos,value, bit_string)
	elif pos == 0:
		string = value
	text += string

f.write(text)
file.close()
f.close()
t1 = time.time()
print(t1-t0)