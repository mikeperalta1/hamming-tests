


import hamming
from bitarray import bitarray


data_bits = input("Enter your data bits ===> ")
codeword_with_overall = hamming.encode(bitarray(data_bits))

codeword_without_overall = codeword_with_overall[1:]


print("Original data bits:", data_bits)
print("Codeword:", codeword_without_overall)



