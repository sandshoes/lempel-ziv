import time
t0 = time.time()
text = open('quijote.txt', 'r', encoding='latin-1')
t = 0
n = 1
alphabet = {}
test = {}
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
			stringer = alphabet[string][1]
			remainder = findpos(string[:-1], alphabet)
		break

	t = 0
	string += x
	if string in alphabet:
		t = 1

	if t != 1:
		pos = n
		n += 1
		value = ' '.join(map(bin,bytearray(x,'latin-1')))
		value = addpadding(value, 8)
		binary_pos = findpos(string[:-1], alphabet)
		alphabet[string] = [pos, value]
		test[string] = binary_pos
		string = ''
		t = 0

psi = len(bin(pos))-2
for i in alphabet:
	stringy = addpadding(test[i],psi) + alphabet[i][1]
	conversion += stringy
conversion += addpadding(remainder,psi) + stringer
extra_padding = 8 - len(conversion) % 8
longitude = addpadding(bin(psi),8)

for i in range(extra_padding):
	conversion += "0"
padded_info = "{0:08b}".format(extra_padding)
conversion = longitude +padded_info + conversion

byte_array = bytearray()
for l in range(0, len(conversion),8):
	byte_array.append(int(conversion[l:l+8], 2))

f.write(bytes(byte_array))
f.close()
t1 = time.time()
print(t1-t0)