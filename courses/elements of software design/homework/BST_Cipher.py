#  File: BST_Cipher.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

#  Description: Utilize BST to encrypt and decrypt messages
#  Date: July 12, 2023

import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        self.root = None
        clean_key = self.clean(key.lower())
        added = ""

        for ch in clean_key:
            if ch in added: # don't add duplicates
                continue
            else:
                self.insert(ch)
                added += ch


    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        self.root = self.insert_helper(self.root, ch)
    
    def insert_helper(self, node, ch):
        if node is None:
            return Node(ch)
        
        if ch < node.ch:
            node.left = self.insert_helper(node.left, ch)
        else:
            node.right = self.insert_helper(node.right, ch)
        return node

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        # remove invalid characters
        encrypted = ""
        clean_message = self.clean(message.lower())

        for ch in clean_message:
            encrypted_ch = self.encrypt_ch(ch)
            encrypted += encrypted_ch
        return encrypted[:-1]

    # Encrypts a single character
    def encrypt_ch(self, ch):
        code = ""

        if ch == self.root.ch:
            code += "*"

        current = self.root
        while current.ch != ch:
            if ch < current.ch: # left of current
                code += "<"
                current = current.left
            else: # right of current
                code += ">"
                current = current.right

        code += "!"
        
        return code

    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        # remove invalid code
        valid_codes_string = ""
        valid_codes = ["<", ">", "*", "!"]
        for i in codes_string:
            if i in valid_codes:
                valid_codes_string += i
        valid_codes_string = valid_codes_string.split("!")
    
        decrypted = ""
        for code in valid_codes_string:
            decrypted_ch = self.decrypt_code(code)
            decrypted += decrypted_ch
        return decrypted
    
    # Decrypts a single code
    def decrypt_code(self, code):
        if code == '*':
            return self.root.ch
        
        current = self.root
        for i in code:
            if current != None:
                if i == "<": # traverse left
                    current = current.left
                else: # traverse right
                    current = current.right
            else:
                return ""
        return current.ch
    

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    # Get clean version of text
    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False



''' ##### DRIVER CODE ##### '''

def main():

    # Debug flag
    debug = True
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
