import string
import random

class GMEncryption:
    def __init__(self):
        self.mapping = None
    
    def generate_mapping(self):
        # Generate a shuffled list of all uppercase and lowercase letters
        letters = list(string.ascii_letters)
        random.shuffle(letters)

        # Create a dictionary that maps each letter to its corresponding shuffled letter
        mapping = {}
        for i in range(len(letters)):
            mapping[string.ascii_letters[i]] = letters[i]

        self.mapping = mapping

    def encrypt(self, text):
        if not self.mapping:
            self.generate_mapping()
        encrypted_text = ''
        for c in text:
            if c.isalpha():
                # Map each letter to its corresponding letter in the randomly generated mapping
                encrypted_text += self.mapping[c]
            else:
                # Leave non-letter characters unchanged
                encrypted_text += c
        return encrypted_text

    def decrypt(self, text):
        if not self.mapping:
            self.generate_mapping()
        # Invert the mapping so we can look up each letter's original value
        inverse_mapping = {v: k for k, v in self.mapping.items()}
        decrypted_text = ''
        for c in text:
            if c.isalpha():
                # Map each letter in the encrypted text back to its original letter using the inverted mapping
                decrypted_text += inverse_mapping[c]
            else:
                # Leave non-letter characters unchanged
                decrypted_text += c
        return decrypted_text