This is a new kind of encryption method! You can use it to for example encode a web user password and its a unknown kind of has no one can decode it except you!

Here is a example of how to use it:

from GMEncryption import GMEncryption


re = GMEncryption()

# Encrypt and decrypt some text
text = 'Hello, world!'
encrypted_text = re.encrypt(text)
decrypted_text = re.decrypt(encrypted_text)

print('Original text:', text)
print('Encrypted text:', encrypted_text)
print('Decrypted text:', decrypted_text)


Hope you enjoy it!