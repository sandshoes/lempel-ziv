import time
t0 = time.time()
text = open('quijote.txt', 'r', encoding='latin-1')
i = 0
t = 0
n = 1
alphabet = {}
string = ''
f = open('compression.txt','wb')
conversion = ''

def addpadding(binchange, length):
	binchange = str(binchange)[2:]
	if len(binchange) < length:
		for y in range(length-len(binchange)):
			binchange = '0'+binchange
	return binchange

def findpos(string, d):
	if string in d:
		s = d[string][0]
		binary_pos = bin(s)
	else:
		binary_pos = bin(0)
	return binary_pos
	
while True:
	x = text.read(1)
	if not x:
		if string in alphabet:
			conversion += alphabet[string][1]
		break
	i += 1
	t = 0
	
	string += x
	if i == 16777216:
		i = 0
		alphabet.clear()
	
	if string in alphabet: 
		t = 1

	if t != 1:
		pos = n
		n += 1
		value = ' '.join(map(bin,bytearray(x,'latin-1')))
		value = addpadding(value, 8)
		binary_pos = findpos(string[:-1], alphabet)
		binary_pos = addpadding(binary_pos, 19)
		alphabet[string] = [pos, binary_pos + value] 
		conversion += alphabet[string][1]
		string = ''
		t = 0

extra_padding = 8 - len(conversion) % 8
for i in range(extra_padding):
	conversion += "0"
padded_info = "{0:08b}".format(extra_padding)
conversion = padded_info + conversion

byte_array = bytearray()
for l in range(0, len(conversion),8):
	byte_array.append(int(conversion[l:l+8], 2))

f.write(bytes(byte_array))
f.close()
t1 = time.time()
print(t1-t0)