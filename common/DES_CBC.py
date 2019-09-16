from random import randint
import ipdb

ip = [57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      56, 48, 40, 32, 24, 16, 8, 0,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6
      ]

expansion_table = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]

pc1 = [56, 48, 40, 32, 24, 16, 8,
       0, 57, 49, 41, 33, 25, 17,
       9, 1, 58, 50, 42, 34, 26,
       18, 10, 2, 59, 51, 43, 35,
       62, 54, 46, 38, 30, 22, 14,
       6, 61, 53, 45, 37, 29, 21,
       13, 5, 60, 52, 44, 36, 28,
       20, 12, 4, 27, 19, 11, 3
       ]
left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

pc2 = [13, 16, 10, 23, 0, 4,
       2, 27, 14, 5, 20, 9,
       22, 18, 11, 3, 25, 7,
       15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54,
       29, 39, 50, 44, 32, 47,
       43, 48, 38, 55, 33, 52,
       45, 41, 49, 35, 28, 31
       ]

fp = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]

sbox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]

p = [
    15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17, 30, 9, 1, 7,
    23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10,
    3, 24
]


def key_generation(key_64):
    subkeys = []
    key_draft = []

    c0 = []
    d0 = []

    key_64_p = [key_64[pc1[i]] for i in range(56)]

    c0 = key_64_p[0:28]
    d0 = key_64_p[28:56]

    for j in range(0, 16):
        for i in range(left_rotations[j]):
            c1 = c0[1:] + c0[:1]
            d1 = d0[1:] + d0[:1]
            c0 = c1[:]
            d0 = d1[:]
        tab_pc2 = c1 + d1

        res_pc2 = [tab_pc2[pc2[i]] for i in range(48)]

        subkeys.append(res_pc2)

    return subkeys


# f applies on function R-1(32bits) and K1(48bits) ,its output is in 32bits
def f(R, K):
    # Expansion D-box 32bits => 48  bits
    R48 = list(range(48))
    for i in range(48):
        R48[i] = R[expansion_table[i]]

    # Whitener R48 XOR K
    after_XOR = [R48[j] ^ K[j] for j in range(48)]

    # S-boxes 8 S-boxes of with 6bits as input
    after_sbox = []
    for j in range(8):
        Sixbits = after_XOR[(j * 6):(j + 1) * 6]
        bits_1_6 = int(str(Sixbits[0]) + str(Sixbits[5]), 2)
        bits_2_5 = int(str(Sixbits[1]) + str(Sixbits[2]) + str(Sixbits[3]) + str(Sixbits[4]), 2)
        found_int = sbox[j][bits_1_6 * 16 + bits_2_5]
        after_sbox += [int(i) for i in bin(found_int)[2:].zfill(4)]
    result = after_sbox[:]
    for i in range(32):
        result[i] = after_sbox[p[i]]
    return result


def DES(plaintext_64, key_64):
    subkeys = key_generation(key_64)
    iptext = plaintext_64[:]

    for i in range(64):
        iptext[i] = plaintext_64[ip[i]]
    L = iptext[:32]
    R = iptext[32:64]
    for i in range(16):
        f_result = f(R, subkeys[i])
        C = R[:]
        R = [L[q] ^ f_result[q] for q in range(32)]
        L = C[:]

    res = R + L
    fptext = res[
             :]  # becareful to the assignment here : fptext=res => it means passing by refernce and fptext=res[:] it means copy by value
    for i in range(64):
        fptext[i] = res[fp[i]]
    print(fptext)
    return fptext


def DES_decrypt(ciphertext, key_64):
    initial_permut = [ciphertext[ip[i]] for i in range(64)]

    L = initial_permut[:32]
    R = initial_permut[32:64]
    subkeys = key_generation(key_64)

    for i in range(15, -1, -1):
        f_result = f(R, subkeys[i])
        C = R[:]
        R = [L[q] ^ f_result[q] for q in range(32)]
        L = C[:]
    # ipdb.set_trace()
    res = R + L

    final_result = [res[fp[i]] for i in range(64)]
    print(final_result)
    return final_result


def CBC_DES_ENC(IV, text,
                key_hexa):  # IV : is a 64 bits binary vector and text : is a string of characteres, key_hexa string of HEX chars
    key_binary = [int(i, 2) for i in bin(int('0x' + key_hexa, 16))[2:].zfill(64)]
    binary_ciphertext_array = []
    binary_text_array = []
    binary_array_of_char = [int(i, 2) for i in bin(ord('a'))[2:].zfill(8)]
    for i in text:
        binary_text_array += [int(i, 2) for i in bin(ord(i))[2:].zfill(8)]
    block_number = len(binary_text_array) / 64
    last_block_size = len(binary_text_array) % 64
    # if(last_block_size!=0) : block_number+=1
    init_vect = IV[:]
    cypher_text = []

    # ipdb.set_trace() # debuging

    for i in range(int(block_number)):
        block = binary_text_array[i * 64:(i + 1) * 64]
        XOR_res = [int(init_vect[j]) ^ block[j] for j in range(64)]
        cipher_block = DES(XOR_res, key_binary)
        cypher_text += cipher_block
        init_vect = cipher_block[:]

    if (last_block_size != 0):
        block_number = block_number + 1
        last_block = binary_text_array[-last_block_size:] + [0] * (64 - last_block_size)
        XOR_res = [init_vect[i] ^ last_block[i] for i in range(64)]
        cipher_block = DES(XOR_res, key_binary)
        cypher_text += cipher_block
    # ipdb.set_trace()
    # cypher_text_hex = hex(int(''.join(map(str, cypher_text)), 2))[2:].zfill(block_number*16)
    cypher_text_ascii_string = [chr(int(
        str(cypher_text[i]) + str(cypher_text[i + 1]) + str(cypher_text[i + 2]) + str(cypher_text[i + 3]) + str(
            cypher_text[i + 4]) + str(cypher_text[i + 5]) + str(cypher_text[i + 6]) + str(cypher_text[i + 7]), 2)) for i
                                in range(0, len(cypher_text) - 1, 8)]

    return cypher_text_ascii_string  # cypher_text_ascii_string : string (a list) of ascii char


def CBC_DES_DEC(IV, cyphertext,
                key_hexa):  # cyphertext : is string (or list of chars) ,IV 64 bits binary vector , key_hexa a string of HEX chars
    key_binary = [int(i, 2) for i in bin(int('0x' + key_hexa, 16))[2:].zfill(64)]
    binary_ciphertext_array = []
    for i in cyphertext:
        binary_ciphertext_array += [int(i, 2) for i in bin(ord(i))[2:].zfill(8)]
    block_number = len(binary_ciphertext_array) / 64
    last_block_size = len(binary_ciphertext_array) % 64

    # ipdb.set_trace()
    block_number = int(block_number)
    init_vect = IV[:]
    text = []
    for i in range(block_number):
        block = binary_ciphertext_array[i * 64:(i + 1) * 64]
        text_block = DES_decrypt(block, key_binary)
        XOR_res = [int(init_vect[i]) ^ text_block[i] for i in range(64)]
        text += XOR_res
        init_vect = block[:]

    text_ascii_string = [chr(int(
        str(text[i]) + str(text[i + 1]) + str(text[i + 2]) + str(text[i + 3]) + str(text[i + 4]) + str(
            text[i + 5]) + str(text[i + 6]) + str(text[i + 7]), 2)) for i in range(0, len(text) - 1, 8)]

    return text_ascii_string  # text_ascii_string : decrypted string (a list of ASCII chars)