import random

# your_word = input("What word would you like to encode?")
# shift = int(input("What number would you like to shift by?"))

rand_fact_list = []

# fun_fact_list = ["there are only 10 types of people in this world, those who understand binary, and those who don't.", "typewriter is the longest word you can write using the letters only on one row of the keyboard of your computer.", "doug engelbart invented the first computer mouse in around 1964 which was made of wood", "there are more than 5000 new computer viruses released every month", "the password for the computer controls of nuclear tipped missiles of the u.s.a. was 00000000 for eight years."]

def fact_picker():
    fun_fact_list = ["there are only 10 types of people in this world, those who understand binary, and those who don't.", "typewriter is the longest word you can write using the letters only on one row of the keyboard of your computer.", "doug engelbart invented the first computer mouse in around 1964 which was made of wood", "there are more than 5000 new computer viruses released every month", "the password for the computer controls of nuclear tipped missiles of the u.s.a. was 00000000 for eight years."]
    rand_num = random.randint(0,4)
    rand_fact = fun_fact_list[rand_num]
    return rand_fact


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# new_word = ""

def encoder(word, shift):
    result_word = ""
    for char in word:
        if char in alphabet:
            index_num = alphabet.index(char)
            new_index = (index_num + shift) % 26
            result_word += alphabet[new_index]
            # print(result_word)
        else:
            result_word += char
    return result_word

def decoder(word, shift, result_word):
    for char in word:
        if char in alphabet:
            index_num = alphabet.index(char)
            new_index = (index_num - shift) % 26
            result_word += alphabet[new_index]
            # print(result_word)
        else:
            result_word += char
    return result_word

        