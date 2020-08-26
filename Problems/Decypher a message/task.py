word = input()
number = int(input())
encode_word = ""
word_decoded = bytes(word, "utf-8")
number_decoded = number.to_bytes(2, "little")
key_number = number_decoded[0] + number_decoded[1]


for byte in word_decoded:
    encode_word += chr(byte + key_number)
    
print(encode_word)
