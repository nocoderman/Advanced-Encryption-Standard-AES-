##AES Encryption
__author__ = "Arnav"

##import statements:
import numpy as np

##static s_box array
s_box = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
         0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
         0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
         0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
         0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
         0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
         0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
         0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
         0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
         0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
         0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
         0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
         0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
         0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
         0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
         0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

##static inverted s_box array
inv_s_box = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
             0x9e, 0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
             0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54,
             0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
             0x42, 0xfa, 0xc3, 0x4e, 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
             0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8,
             0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
             0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
             0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84, 0x90, 0xd8, 0xab,
             0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
             0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
             0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41,
             0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
             0x73, 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
             0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1, 0x1a, 0x71, 0x1d,
             0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
             0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
             0xfe, 0x78, 0xcd, 0x5a, 0xf4, 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
             0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f, 0x60,
             0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
             0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
             0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61, 0x17, 0x2b,
             0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
             0x21, 0x0c, 0x7d]

##static round counter array (Key Expansion)
r_con = [0x01, 0x02,
         0x04, 0x08, 0x10,
         0x20, 0x40, 0x80,
         0x1b, 0x36]


##rotate each byte one position to the left
def rotate_left(word):
    return word[1:] + word[:1]


##xtime implementation
def xtime_function(a):
    for i in range(1):
        if a & 0x80:
            a = a << 1
            ##hex rep for AES polynomial (100011011)
            a ^= 0x1B
        else:
            a = a << 1
    return a & 0xFF


##key expansion for AES-128
def key_expansion128(init_key):
    ##16, 24, 32 - lengths
    ExpansionKey = init_key
    round_counter = 0

    while len(ExpansionKey) < 176:
        for j in range(4):
            temp1 = ExpansionKey[-4:]
            if j == 0:
                ##key expansion core
                temp1 = rotate_left(temp1)
                for k in range(len(temp1)):
                    temp1[k] = s_box[temp1[k]]
                temp1[0] = temp1[0] ^ r_con[round_counter]
            temp2 = ExpansionKey[-16:-12]
            for l in range(4):
                ExpansionKey.append(temp1[l] ^ temp2[l])
        round_counter += 1

    return ExpansionKey


##key expansion for AES-192
def key_expansion192(init_key):
    ExpansionKey = init_key
    round_counter = 0
    while len(ExpansionKey) < 208:
        for j in range(6):
            temp1 = ExpansionKey[-4:]
            if j == 0:
                ##key expansion core
                temp1 = rotate_left(temp1)
                for k in range(len(temp1)):
                    temp1[k] = s_box[temp1[k]]
                temp1[0] = temp1[0] ^ r_con[round_counter]
            temp2 = ExpansionKey[-24:-20]
            for l in range(4):
                ExpansionKey.append(temp1[l] ^ temp2[l])
        round_counter += 1

    return ExpansionKey


##key expansion for AES-256
def key_expansion256(init_key):
    ExpansionKey = init_key
    round_counter = 0
    while len(ExpansionKey) < 240:
        for j in range(8):
            temp1 = ExpansionKey[-4:]
            if j == 0:
                ##key expansion core
                temp1 = rotate_left(temp1)
                for k in range(len(temp1)):
                    temp1[k] = s_box[temp1[k]]
                temp1[0] = temp1[0] ^ r_con[round_counter]
            if j == 4:
                for i in range(len(temp1)):
                    temp1[i] = s_box[temp1[i]]

            temp2 = ExpansionKey[-32:-28]
            for l in range(4):
                ExpansionKey.append(temp1[l] ^ temp2[l])

        round_counter += 1

    return ExpansionKey


##convert a string of input key to a list of int values
def key_mod(init_key):
    split_key = [(init_key[i:i + 2]) for i in range(0, len(init_key), 2)]
    for i in range(len(split_key)):
        split_key[i] = int(split_key[i], 16)
    return split_key


##XOR's a round key to a specified block
def add_round_key(block, round_key):
    ##use key mod for debugging
    # block = key_mod(block)
    # round_key = key_mod(round_key)
    ##----------------------------------------
    temp_block = []
    temp_round_key = []
    while block:
        temp_block.append(block[:4])
        block = block[4:]
    while round_key:
        temp_round_key.append(round_key[:4])
        round_key = round_key[4:]
    final_arr = []
    ##add cbc flag here:
    for i in range(4):
        for j in range(4):
            final_arr.append(temp_block[i][j] ^ temp_round_key[i][j])
    return final_arr


##shifts matrix rows by a certain number
def shift_rows(block):
    temp_block = []
    while block:
        temp_block.append(block[:4])
        block = block[4:]

    ##transpose the matrix to fix the row-column error
    data = np.array(temp_block).T

    ##shift second row one byte to the left
    data[1] = np.roll(data[1], -1)

    ##shift third row two bytes to the left
    data[2] = np.roll(data[2], -2)

    ##shift fourth row three bytes to the left
    data[3] = np.roll(data[3], -3)

    return data


##inverse shift matrix implementation
def inv_shift_rows(block):
    # parse the 4x4 block as a numpy array
    data = np.array(block)
    data[1] = np.roll(data[1], 1)
    data[2] = np.roll(data[2], 2)
    data[3] = np.roll(data[3], 3)

    ##convert 4x4 to a list
    final_shift_arr = []
    for x in range(len(data)):
        for y in range(len(data)):
            final_shift_arr.append(data[y][x])

    return final_shift_arr


##multiplies a constant 4x4 matrix with a 4x1 column vector from the message block
##if flag == true, returns mix_columns format (list) else returns a 4x4 nested list for inv_matrix_column
def mix_columns(block, flag):
    temp = [[], [], [], []]
    for i in range(4):
        col = [block[j][i] for j in range(4)]
        col = mix_columns_helper(col)
        for k in range(4):
            temp[k].append(col[k])
    mix_arr = []
    if flag:
        for x in range(len(temp)):
            for y in range(len(temp)):
                mix_arr.append(temp[y][x])
        return mix_arr
    else:
        return temp


##helper function for mix columns
def mix_columns_helper(column):
    mat = [
        xtime_function(column[0]) ^ xtimeOR(
            column[1]) ^ column[2] ^ column[3],
        xtime_function(column[1]) ^ xtimeOR(
            column[2]) ^ column[3] ^ column[0],
        xtime_function(column[2]) ^ xtimeOR(
            column[3]) ^ column[0] ^ column[1],
        xtime_function(column[3]) ^ xtimeOR(
            column[0]) ^ column[1] ^ column[2],
    ]
    return mat


##XORs the xtime function with a specified block
def xtimeOR(a):
    return xtime_function(a) ^ a


##inverse mix columns implementation
def inv_mix_columns(matrix_list):
    nested_list = [[], [], [], []]

    ##convert list to a 4x4 nested list
    for i in range(4):
        for j in range(4):
            nested_list[i].append(matrix_list[4 * j + i])

    inverse_matrix = mix_columns(mix_columns(nested_list, False), False)
    inverse_matrix = mix_columns(inverse_matrix, False)

    return inverse_matrix


##byte replacements for s_box lookup table
def sub_bytes(block):
    for i in range(len(block)):
        block[i] = s_box[block[i]]
    return block


##byte replacements for inv_s_box lookup table
def inv_sub_bytes(block):
    for i in range(len(block)):
        block[i] = inv_s_box[block[i]]
    return block


##gets the key set from the expanded key based on the round key
def get_expanded_key_set(expanded_key, round_number):
    if round_number == 0:
        expanded_key = expanded_key[:16]
    else:
        expanded_key = expanded_key[16 * round_number: 32 * round_number]

        ##add an error check if round_number is greater than the intended one
        if not expanded_key:
            print(str(round_number), "exceeds expanded key size")
    return expanded_key


##Main encryption method
def encryption(plaintext, key, CBC):
    plaintext = key_mod(plaintext)
    set_rounds = 0
    expanded_key = None
    ##check key lengths to determine which key expansion should be called
    if len(key) == 32:
        expanded_key = key_expansion128(key_mod(key))
        set_rounds = 10

    elif len(key) == 48:
        expanded_key = key_expansion192(key_mod(key))
        set_rounds = 12

    elif len(key) == 64:
        expanded_key = key_expansion256(key_mod(key))
        set_rounds = 14

    else:
        print("Invalid Key Size")

    nested_ciphertext = []
    final_ark = None

    while len(plaintext) > 0:
        get_key = get_expanded_key_set(expanded_key, 0)
        ark = add_round_key(plaintext, get_key)

        ##add a CBC condition to modify the first add round key for each block
        if CBC:
            if final_ark is not None:
                ark = add_round_key(final_ark, ark)

        for i in range(1, set_rounds):
            substitution = sub_bytes(ark)
            shift_row = shift_rows(substitution)
            mix_column = mix_columns(shift_row, True)
            get_key = get_expanded_key_set(expanded_key, i)
            ark = add_round_key(mix_column, get_key)

        final_substitution = sub_bytes(ark)
        final_shift = shift_rows(final_substitution)

        ##convert shift_rows into array form
        final_shift_arr = []
        for x in range(len(final_shift)):
            for y in range(len(final_shift)):
                final_shift_arr.append(final_shift[y][x])

        final_key = get_expanded_key_set(expanded_key, set_rounds)
        final_ark = add_round_key(final_shift_arr, final_key)

        nested_ciphertext.append(final_ark)
        plaintext = plaintext[16:]

    final_encryption = []
    for sublist in nested_ciphertext:
        for item in sublist:
            final_encryption.append(item)
    return hex_to_string(int_to_hex(final_encryption))


##Main decryption method
def decryption(ciphertext, key, CBC):
    ciphertext = key_mod(ciphertext)
    set_rounds = 0
    expanded_key_decrypt = None
    ##check key lengths to determine which key expansion should be called
    if len(key) == 32:
        expanded_key_decrypt = key_expansion128(key_mod(key))
        set_rounds = 10

    elif len(key) == 48:
        expanded_key_decrypt = key_expansion192(key_mod(key))
        set_rounds = 12

    elif len(key) == 64:
        expanded_key_decrypt = key_expansion256(key_mod(key))
        set_rounds = 14
    else:
        print("Invalid Key Size")

    temp_array = []
    ciphertext_copy = None
    while len(ciphertext) > 0:
        get_key = get_expanded_key_set(expanded_key_decrypt, set_rounds)
        ark = add_round_key(ciphertext, get_key)

        nested_list = [[], [], [], []]
        ##convert list to a 4x4 nested list
        for i in range(4):
            for j in range(4):
                nested_list[i].append(ark[4 * j + i])
        initial_shift = inv_shift_rows(nested_list)
        inverse_substitution = inv_sub_bytes(initial_shift)

        for j in range(set_rounds - 1, 0, -1):
            get_key = get_expanded_key_set(expanded_key_decrypt, j)
            ark = add_round_key(inverse_substitution, get_key)
            inv_mix_col = inv_mix_columns(ark)
            inv_shift_row = inv_shift_rows(inv_mix_col)
            inverse_substitution = inv_sub_bytes(inv_shift_row)

        final_key = get_expanded_key_set(expanded_key_decrypt, 0)
        final_ark = add_round_key(inverse_substitution, final_key)
        if CBC:
            if ciphertext_copy is not None:
                final_ark = add_round_key(ciphertext_copy, final_ark)

        ciphertext_copy = ciphertext

        temp_array.append(final_ark)
        ciphertext = ciphertext[16:]

    final_decryption = []
    for sublist in temp_array:
        for item in sublist:
            final_decryption.append(item)
    return hex_to_string(int_to_hex(final_decryption))


##Converts array in base int to hex
def int_to_hex(arr):
    temp_rep = [hex(x) for x in arr]
    return temp_rep


##final formatting: converts list of hex to a proper string hex
def hex_to_string(array):
    remove_0_x = []
    ##remove '0's and 'x's from the list
    for hexes in array:
        remove_0_x.append(hexes[2:])

    ##check length of elements and pad a zero for size = 1 elements
    pad_length = []
    for value in remove_0_x:
        if len(value) != 2:
            leading_zero = value.zfill(2)
            value = value.replace(value, leading_zero)
        pad_length.append(value)

    ##merge the list into a single string
    final_string = "".join(pad_length)
    return final_string


##_________________________________________________________________________________________________________________

##CODE COMPILER:
##Change the CBC flags based on which mode you need for encryption and decryption
##(True to enable CBC mode, False to enable ECB mode)

CBC_encryption = False
CBC_decryption = True

##-----------------------------
##Do not modify this cell!
if not CBC_encryption:
    text_encryption = "(ECB)"
else:
    text_encryption = "(CBC)"

if not CBC_decryption:
    text_decryption = "(ECB)"
else:
    text_decryption = "(CBC)"
##----------------------------
##Change arguments 1 and 2 in the print functions itself, argument 3 can be changed from the CBC flags.

##Encryption:
##argument 1: plain text, argument 2: key, argument 3: CBC boolean
print("Ciphertext after encryption " + text_encryption + ":",
      encryption(
          "0123456789abcdef0123456789abcdef",
          "f839739fff1d95775ebcd6d16586ccacd4eadfcae84b1643",
          CBC_encryption))

##Decryption:
##argument 1: cipher text, argument 2: key, argument 3: CBC boolean
print("Plaintext after decryption " + text_decryption + ":",
      decryption(
          "a5360648c5a07b8b0d32526666d6956740ff173728e3873e0f369e0eccdaf8b5707e16aa4879b76e81719c449e710b8f003140671445d240e4223fa7d10f834774496b0c743721f6e7cb222b5a69a41aa37370002db9a29e7301013960c91068",
          "4e0e01285b1ff23909b11b5de4ea01c11acf4a713a66f782",
          CBC_decryption))
