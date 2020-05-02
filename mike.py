


import hamming
from bitarray import bitarray


print("Welcome to simple Hamming SEC/DED encoding/decoding")


def the_loop():

	did_anything = False

	print()
	data_bits = input("Enter some data bits to encode (blank to skip this part) ===> ")
	if data_bits != "":

		did_anything = True

		codeword = hamming.encode(bitarray(data_bits))

		print("Original data bits:", data_bits)
		print("Codeword:", codeword_with_overall)
		print()

	print()
	codeword = input("Enter a codeword to decode (blank to skip this part) ===> ")
	if codeword != "":

		did_anything = True

		codeword = bitarray(codeword)
		data_bits = hamming.decode(codeword)

		print("Original codeword:", codeword)
		print("Decoded data bits:", data_bits)
		print()

	return did_anything


while the_loop():
	pass
print("Did nothing last loop; Quitting")




