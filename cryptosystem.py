# Eric Anderson
# Alex Mclennan
# Mahimna Dave


def open_file(info):
    file_string = ''
    the_filename = ""
    try:
        for i in range(len(info)):
            if i == len(info) - 1:
                the_filename += info[i]
            elif i > 0:
                the_filename += info[i] + " "
        file_size = path.getsize(the_filename + ".txt")
        if file_size == 0:
            print("\u001b[31mThe file is empty and therefore cannot be opened\n\u001b[0m")
            the_filename = ""
        else:
            file_string = open("{}.txt".format(the_filename), encoding="utf8").read()
    except FileNotFoundError:
        print("\u001b[31mError: The file [", the_filename, "] does not exist\n\u001b[0m")
    return [the_filename, file_string]


def make_key():
    date1 = str(datetime.now())
    base_key = ''
    for i in range(len(date1)):
        if date1[i] != ':' and date1[i] != '-' and date1[i] != ' ' and date1[i] != '.':
            base_key += date1[i]

    found_dot = False
    milliseconds = ''
    for i in range(len(date1)):
        if found_dot:
            milliseconds += date1[i]
        if date1[i] == '.':
            found_dot = True

    time.sleep(int(milliseconds)/1000000)

    date2 = str(datetime.now())
    found_dot = False
    multiplier = ''
    for i in range(len(date2)):
        if found_dot:
            multiplier += date2[i]
        if date2[i] == '.':
            found_dot = True

    pre_key = str(math.sqrt(math.lgamma(int(base_key) * int(multiplier))))
    key = ''
    for i in range(17):
        try:
            if pre_key[i] != '.':
                key += pre_key[i]
        except IndexError:
            key += '0'
    return key


def block_text(key, block_size, data1, the_mode=1):
    block_list = []
    block_chunk = []
    if the_mode == 1:
        punc = '#'
    elif the_mode == 2:
        punc = []
        plugin_size = int(key[0]) if int(key[0]) > 2 else 3
        for i in range(plugin_size):
            punc.append('^')

    for char in data1:
        block_chunk.append(char)

        if len(block_chunk) == int(block_size):
            block_list.append(block_chunk.copy())
            block_chunk.clear()

    else:
        if block_chunk:
            while len(block_chunk) != int(block_size):
                block_chunk.append(punc)
            else:
                block_list.append(block_chunk)
    return block_list


def text_scramble_encrypt(key, data2, the_mode=1):
    key = [num for num in key]
    if the_mode == 1:
        block_size = key[0] if int(key[0]) > 2 else '3'
        block_list = block_text(key, block_size, data2)
        scramble_key = key[1:int(block_size) + 1]
    elif the_mode == 2:
        if int(key[10]) < 3 or int(key[10]) > 5:
            if int(key[10]) <= 2:
                block_size = '3'
            else:
                block_size = '5'
        else:
            block_size = key[10]
        block_list = block_text(key, block_size, data2, 2)
        scramble_key = key[11:int(block_size) + 11]

    scrambled_block_list = []
    scramble_key_sorted_list = sorted(scramble_key)

    # For each block in block_list
    for block in block_list:
        # Copies the actual key
        tmp_key = scramble_key.copy()  # Temporary key var of key
        scrambled_block = []  # Will be the new block

        # For every num in sorted list
        for num in scramble_key_sorted_list:
            index = int(tmp_key.index(num))  # Get's the index of the num in the temporary key var
            tmp_key.pop(index)  # Gets rid of the num
            to_add = block.pop(int(index))  # Pops the letter out and grabs it
            scrambled_block.append(to_add)  # Adds that index of the block to the new block

        # Adds the new block to the total blocks
        else:
            scrambled_block_list.append(scrambled_block)
    return scrambled_block_list


def text_scramble_decrypt(key, data2, the_mode=1):
    key = [num for num in key]
    if the_mode == 1:
        block_size = key[0] if int(key[0]) > 2 else '3'
        block_list = block_text(key, block_size, data2)
        scramble_key = key[1:int(block_size) + 1]
    elif the_mode == 2:
        if int(key[10]) < 3 or int(key[10]) > 5:
            if int(key[10]) <= 2:
                block_size = '3'
            else:
                block_size = '5'
        else:
            block_size = key[10]
        block_list = block_text(key, block_size, data2, 2)
        scramble_key = key[11:int(block_size) + 11]

    scramble_key_sorted = sorted(scramble_key)

    unscramble_key = []
    tmp_scramble_key_sorted = scramble_key_sorted.copy()
    for i in range(len(scramble_key)):
        index = tmp_scramble_key_sorted.index(scramble_key[i])
        unscramble_key.append(index)
        tmp_scramble_key_sorted[index] = '10'

    unscrambled_list = []
    for block in block_list:
        if the_mode == 1:
            unscrambled_text = ''
        elif the_mode == 2:
            unscrambled_text = []
        for i in range(len(block)):
            if the_mode == 1:
                unscrambled_text += block[unscramble_key[i]]
            elif the_mode == 2:
                unscrambled_text.append(block[unscramble_key[i]])
        unscrambled_list.append(unscrambled_text)
    return unscrambled_list


def binary_flip_1(data):
    output = ''
    for i in data:
        ascii_int = ord(i)
        if ascii_int % 2 == 0:
            ascii_int += 1
            output += chr(ascii_int)
        else:
            ascii_int -= 1
            output += chr(ascii_int)
    return output


def binary_flip_2(key, data):
    key_list = list(key)
    count = 1
    index = 0
    output = ''
    for i in data:
        if int(key_list[index]) == 0:
            key_val = 1
        else:
            key_val = int(key_list[index])

        if count == key_val:
            ascii_int = ord(i)
            if ascii_int % 2 == 0:
                ascii_int += 1
                output += chr(ascii_int)
            else:
                ascii_int -= 1
                output += chr(ascii_int)
            count = 1
            if index >= 15:
                index = 0
            else:
                index += 1
        else:
            output += i
            count += 1
    return output


def crypto_system(key, data):
    text_scramble_to_string = ''
    for i in text_scramble_encrypt(key, text_scramble_encrypt(key, data), 2):
        for j in i:
            for z in j:
                text_scramble_to_string += z

    binary_data_encrypt = binary_flip_1(text_scramble_to_string)
    encrypted_text = binary_flip_2(key, binary_data_encrypt)

    print('\u001b[35m')
    print('Key: ' + key)
    print('Data: ' + str(encrypted_text))
    print("\u001b[0m")
    return encrypted_text


def crypto_system_decrypt(key, data):
    binary_data_decrypt1 = binary_flip_1(data)
    binary_data_decrypt2 = binary_flip_2(key, binary_data_decrypt1)

    text_scramble_to_string = ''
    for i in text_scramble_decrypt(key, text_scramble_decrypt(key, binary_data_decrypt2), 2):
        for j in i:
            for z in j:
                text_scramble_to_string += z

    decrypted_text = ''
    for i in text_scramble_to_string:
        if i != '#' and i != '^':
            decrypted_text += i
    print('\u001b[35m')
    print('Data: ' + str(decrypted_text))
    print("\u001b[0m")
    return decrypted_text


if __name__ == "__main__":
    from os import path
    from os import system
    from random import randint
    from art import text2art
    from datetime import datetime
    import time
    import math

########################################################################################################################
    system("cls")
########################################################################################################################
    file_data = []
    file_data_original = []
    operations = []
    index_tracker = 0
    filename = ""
########################################################################################################################
    fonts = ["1943", "3-d", "3d_diagonal", "4max", "5lineoblique", "6x10", "a_zooloo", "alligator2",
             "alligator3", "amcaaa01", "amcneko", "amcslash", "arrows", "ascii_new_roman", "avatar", "basic", "bell",
             "big", "bigfig", "bolger", "braced", "bulbhead", "calgphy2", "chiseled", "chunky", "crawford", "cricket",
             "cyberlarge", "cybermedium", "defleppard", "doom", "double", "epic", "filter", "fire_font-s", "fraktur",
             "georgia11", "ghost", "ghoulish", "graffiti", "isometric1", "isometric4", "jacky", "larry3d", "lean",
             "lineblocks", "merlin1", "modular", "rammstein", "red_phoenix", "rounded", "slant", "speed", "starwars",
             "stop", "sub-zero", "swampland", "twisted"]
    the_font = fonts[randint(0, len(fonts) - 1)]
    text = text2art("CryptoSystem", font=the_font)
    print("\u001b[46;1m\u001b[37;255m", text, "\u001b[0m")
    print("\u001b[34m            By: Eric Anderson"
          "\n                   Alex Mclennan"
          "\n                      Mahimna Dave     \u001b[0m")
    print("\n\n")
    print("Type 'help' to show commands\n")
########################################################################################################################
    while True:
        command = input(">>> ")
        command_info = command.split(" ")
########################################################################################################################
        if command_info[0] == "help":
            print("\u001b[32m"
                  "file <directory>\<file>                 Select a file to open. Do not include file the extension\n"
                  "crypto                                  Encrypts a file\n"
                  "decrypto <key>                          Decrypts a file\n"
                  "print                                   Prints the current text\n"
                  "print original                          Prints the original file text\n"
                  "print key                               Prints the the key for the file if it has one\n"
                  "cls                                     Clears the screen\n"
                  "save                                    Save to original file (Overwrites Current File Data)\n"
                  "save as <directory>\<file>              Save data to a new file. Do not include file the extension\n"
                  "end                                     Ends the program\n"
                  "\u001b[0m")
########################################################################################################################
        elif command_info[0] == "file":
            try:
                file_info = open_file(command_info)
                filename = file_info[0]
                file_data = file_info[1]
                file_data_original = file_info[1]
            except OSError:
                print("\u001b[31mError: The file [", filename, "] does not exist\n\u001b[0m")
########################################################################################################################
        elif command_info[0] == "crypto":
            the_key = make_key()
            file_data = crypto_system(the_key, file_data)
########################################################################################################################
        elif command_info[0] == "decrypto":
            if len(command_info) == 2:
                file_data = crypto_system_decrypt(command_info[1], file_data)
            else:
                print("\u001b[31mError:", command, "is not a command\n\u001b[0m")
########################################################################################################################
        elif command_info[0] == "print":
            print("\u001b[35m")
            if len(command_info) == 2:
                if command_info[1] == "original":
                    for a in file_data_original:
                        print(a.strip("\n"))
                elif command_info[1] == "key":
                    try:
                        print("Key: " + the_key)
                    except NameError:
                        print("\u001b[31mError: There is no key to print\n\u001b[0m")
                else:
                    print("\u001b[31mError:", command_info[1], "is not a command\n\u001b[0m")
            elif len(command_info) == 1:
                print(file_data)
            else:
                print("\u001b[31mError:", command, "is not a command\n\u001b[0m")
            print("\u001b[0m")
########################################################################################################################
        elif command_info[0] == "cls" and len(command_info) == 1:
            system('cmd /c "cls"')
            print("\n\nType 'help' to show commands\n")
########################################################################################################################
        elif command_info[0] == "save":
            if len(command_info) > 1:
                if command_info[1] == "as":
                    endingDirectory = ""
                    for a in range(len(command_info)):
                        if a == len(command_info) - 1:
                            endingDirectory += command_info[a]
                        elif a > 1:
                            endingDirectory += command_info[a] + " "
                    try:
                        endingFile = open("{}.txt".format(endingDirectory), "w", encoding="utf8")
                        endingFile.write(file_data)
                        print("\u001b[32mComplete!\n\u001b[0m")
                        endingFile.close()
                    except OSError:
                        print("\u001b[31m[" + endingDirectory + "] is not a valid file\u001b[0m")
                else:
                    print("\u001b[31mError:", command_info[1], "is not a command\n\u001b[0m")
            else:
                overwrite = input("\u001b[33mAre your sure you want to overwrite " + filename + ".txt\u001b[0m\n>>> ")
                while True:
                    if overwrite.lower() == "yes" or overwrite.lower() == "y":
                        endingFile = open(filename + ".txt", "w", encoding="utf8")
                        endingFile.write(file_data)
                        print("\u001b[32mComplete!\n\u001b[0m")
                        endingFile.close()
                        break
                    elif overwrite.lower() == "no" or overwrite.lower() == "n":
                        break
                    else:
                        overwrite = input("\u001b[31mError: Invalid Input\u001b[0m\n\n>>> ")
########################################################################################################################
        elif command_info[0] == "end" and len(command_info) == 1:
            break
########################################################################################################################
        else:
            command_error = True
            for a in range(len(command_info)):
                if not command_info[a]:
                    command_error = False
                else:
                    command_error = True
            if command_error is True:
                print("\u001b[31mError:", command_info[0], "is not a command\n\u001b[0m")
