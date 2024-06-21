import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '?', '/', ':', ';']

print(art.logo)

directionx = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
textx = input("Type your message:\n").lower()
keyx = input("Type your Key:\n").lower()

def vinegere_encode(text, key):
    edited_text = ''
    for j in range(len(text)):
        if j > (len(key)-1):
            key_mod = j
            key_mod = (key_mod % len(key))
            key_step = alphabet.index(key[key_mod])
        else: 
            key_step = alphabet.index(key[j])
        
        if text[j] == " ":
            edited_text += " "
        elif text[j] in numbers:
            temp = int(text[j])
            temp += key_step
            edited_text += str(temp)
        elif text[j] in symbols:
            edited_text += text[j]
        else:
            step = alphabet.index(text[j])
            step = step + key_step
            if step > 25 or step < 0:
                step = step % 26
            edited_text += alphabet[step]

    print(f"the Encoded Text is :{edited_text}")

def vinegere_decode(text, key):
    edited_text = ''
    for j in range(len(text)):
        if j > (len(key)-1):
            key_mod = j
            key_mod = (key_mod % len(key))
            key_step = alphabet.index(key[key_mod])
        else: 
            key_step = alphabet.index(key[j])

        if text[j] == " ":
            edited_text += " "
        elif text[j] in numbers:
            temp = int(text[j])
            temp -= key_step
            edited_text += str(temp)
        elif text[j] in symbols:
            edited_text += text[j]
        else:
            step = alphabet.index(text[j])
            step = step - key_step
            if step > 25 or step < 0:
                step = step % 26
            edited_text += alphabet[step]

    print(f"the Decoded Text is :{edited_text}")

if directionx=="encode":
    vinegere_encode(text=textx,key=keyx)
else:
    vinegere_decode(text=textx,key=keyx)
