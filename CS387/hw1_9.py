import numpy as np
C1 = '1010110010011110011111101110011001101100111010001111011101101011101000110010011000000101001110111010010111100100111101001010000011000001010001001001010000000010101001000011100100010011011011011011010111010011000101010111111110010011010111001001010101110001111101010000001011110100000000010010111001111010110000001101010010110101100010011111111011101101001011111001101111101111000100100001000111101111011011001011110011000100011111100001000101111000011101110101110010010100010111101111110011011011001101110111011101100110010100010001100011001010100110001000111100011011001000010101100001110011000000001110001011101111010100101110101000100100010111011000001111001110000011111111111110010111111000011011001010010011100011100001011001101110110001011101011101111110100001111011011000110001011111111101110110101101101001011110110010111101000111011001111'
C2 = '1011110110100110000001101000010111001000110010000110110001101001111101010000101000110100111010000010011001100100111001101010001001010001000011011001010100001100111011010011111100100101000001001001011001110010010100101011111010001110010010101111110001100010100001110000110001111111001000100001001010100011100100001101010101111000100001111101111110111001000101111111101011001010000100100000001011001001010000101001110101110100001111100001011101100100011000110111110001000100010111110110111010010010011101011111111001011011001010010110100100011001010110110001001000100011011001110111010010010010110100110100000111100001111101111010011000100100110011111011001010101000100000011111010010110111001100011100001111100100110010010001111010111011110110001000111101010110101001110111001110111010011111111010100111000100111001011000111101111101100111011001111'

BITS_PER_LETTER = 7
N_CHARACTERS = 26
EXPECTED_LETTER_FREQS = np.asarray([       8.167,\
                                           1.492,\
                                           2.782,\
                                           4.253,\
                                           12.702,\
                                           2.228,\
                                           2.015,\
                                           6.094,\
                                           6.966,\
                                           0.153,\
                                           0.772,\
                                           4.025,\
                                           2.406,\
                                           6.749,\
                                           7.507,\
                                           1.929,\
                                           0.095,\
                                           5.987,\
                                           6.327,\
                                           9.056,\
                                           2.758,\
                                           0.978,\
                                           2.360,\
                                           0.150,\
                                           1.974,\
                                           0.074])
CHARACTER_MAPS = {\
                    ord('a') : 0,\
                    ord('b') : 1,\
                    ord('c') : 2,\
                    ord('d') : 3,\
                    ord('e') : 4,\
                    ord('f') : 5,\
                    ord('g') : 6,\
                    ord('h') : 7,\
                    ord('i') : 8,\
                    ord('j') : 9,\
                    ord('k') : 10,\
                    ord('l') : 11,\
                    ord('m') : 12,\
                    ord('n') : 13,\
                    ord('o') : 14,\
                    ord('p') : 15,\
                    ord('q') : 16,\
                    ord('r') : 17,\
                    ord('s') : 18,\
                    ord('t') : 19,\
                    ord('u') : 20,\
                    ord('v') : 21,\
                    ord('w') : 22,\
                    ord('x') : 23,\
                    ord('y') : 24,\
                    ord('z') : 25,\
                 }

def string_to_letter_freq(string):
    obs = np.zeros(N_CHARACTERS) # empty vector for observed freqs
    for letter in string:
        obs[CHARACTER_MAPS[ord(letter.lower())]] += 1
    # scale to percentage
    obs *= 100./np.sum(obs)
    return obs

def bits_to_letter(bits):
    letter_code = 0
    n = len(bits) - 1
    for bit in bits:
        if bit == '1':
            letter_code += 2**n
        n -= 1
    return chr(letter_code)

def bits_to_letter(bits):
    letter_code = 0
    n = len(bits) - 1
    for bit in bits:
        if bit == '1':
            letter_code += 2**n
        n -= 1
    return chr(letter_code)

def bit_string_to_letter_string(bits):
    letter_string = ''
    n_letters = len(bits) / BITS_PER_LETTER
    for i in range(n_letters):
        letter_string += bits_to_letter(bits[i*BITS_PER_LETTER:(i+1)*BITS_PER_LETTER])
    return letter_string

def letter_string_to_bit_string(letters):
    bits = ''
    for letter in letters:
        letter_code = ord(letter)
        if letter_code >= 2**6:
            bits += '1'
            letter_code -= 2**6
        else:
            bits += '0'
        if letter_code >= 2**5:
            bits += '1'
            letter_code -= 2**5
        else:
            bits += '0'
        if letter_code >= 2**4:
            bits += '1'
            letter_code -= 2**4
        else:
            bits += '0'
        if letter_code >= 2**3:
            bits += '1'
            letter_code -= 2**3
        else:
            bits += '0'
        if letter_code >= 2**2:
            bits += '1'
            letter_code -= 2**2
        else:
            bits += '0'
        if letter_code >= 2**1:
            bits += '1'
            letter_code -= 2**1
        else:
            bits += '0'
        if letter_code >= 2**0:
            bits += '1'
            letter_code -= 2**0
        else:
            bits += '0'
    return bits

def compare_freqs(obs, exp):
    pass

if __name__ == '__main__':
    test = 'hello'
    print string_to_letter_freq(test)
    print letter_string_to_bit_string(test)
    x = letter_string_to_bit_string(test)
    print bit_string_to_letter_string(letter_string_to_bit_string(test))
    

    print bits_to_letter('1101000')
    
