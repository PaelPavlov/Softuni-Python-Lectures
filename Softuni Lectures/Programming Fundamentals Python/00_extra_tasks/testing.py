def decipher_secret_message(secret_message):
    words = secret_message.split()
 
    deciphered_words = []
    for word in words:
        if len(word) > 1:
            word = word[0] + word[-1] + word[2:-1] + word[1]
        if word[:-1].isdigit():
            char_code = int(word[:-1])
            word = chr(char_code) + word[-1]
 
        deciphered_words.append(word)
 
    deciphered_message = ' '.join(deciphered_words)
    return deciphered_message
secret_message = input()
deciphered_message = decipher_secret_message(secret_message)
print(deciphered_message)