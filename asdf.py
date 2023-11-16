password_provide=bytes(key,'utf-8')
password=(base64.urlsafe_b64encode(password_provide))
k=Fernet(bytes((password, encodin:='utf-8')))

def encrypt(message, key):
    text_file=open("Test.txt", "w")
    title = title_entry.get()
    add_title = text_file.write(title)
    encrypted=k.encrypt(encoded)
    msg=text_file.write(encrypted)
    for chars in message:
        if chars in message:
            num = message.find(chars)
            num += key
            encrypted +=  message[num]
    print(encrypt(message, key))
    return encrypted

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in message:
            num = message.find(chars)
            num += key
            decrypted += message[num]
    print(encrypt(message, key))

    pass_phrase = key
    used = {' ', '\n'}
    passed = []
    text_file = open("Test.txt", "w")
    title = title_entry.get()
    for c in pass_phrase.upper() + ascii_uppercase:
        if c not in used:
            list(passed).append(c)
            used.add(c)
            passed = ''.join(passed)
            encode = {u: v for u, v in zip(ascii_uppercase, passed)}
            decode = {v: u for u, v in zip(ascii_uppercase, key)}