from math import gcd
from tkinter import *  #GUI Library
from tkinter import messagebox  #Type of GUI 
import base64  #Encryption/Decryption Library

# Global variables for RSA keys
n = 0
e = 0
d = 0

def RSA(p: int, q: int, message: int):
    global n, e, d

    # calculating n
    n = p * q

    # calculating totient, t
    t = (p - 1) * (q - 1)

    # selecting public key, e
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    # selecting private key, d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

# ... (باقي الكود الخاص بالواجهة كما هو) ...

def generate_rsa_keys():
    # ... (كود توليد قيم p و q عشوائياً) ...
    RSA(p, q, 0)  # Generate keys without encrypting a message
    public_key_field.delete(0, END)
    public_key_field.insert(0, f"Public Key: (e, n) = ({e}, {n})")
    private_key_field.delete(0, END)
    private_key_field.insert(0, f"Private Key: (d, n) = ({d}, {n})")

def encrypt():
    if encryption_method.get() == "RSA":
        try:
            message_int = int(text1.get(1.0, END))
            ct = (message_int ** e) % n
            encrypted_text2.delete(1.0, END)
            encrypted_text2.insert(1.0, base64.b64encode(str(ct).encode("ascii")).decode("ascii"))  # Use base64 for display
        except ValueError:
            messagebox.showerror("Error", "Invalid message for RSA encryption. Please enter an integer.")
    else:
        # ... (كود التشفير باستخدام base64 كما هو) ...

def decrypt():
    if decryption_method.get() == "RSA":
        try:
            ct_int = int(base64.b64decode(text2.get(1.0, END)).decode("ascii"))  # Decode from base64
            mes = (ct_int ** d) % n
            decrypted_text2.delete(1.0, END)
            decrypted_text2.insert(1.0, str(mes))
        except ValueError:
            messagebox.showerror("Error", "Invalid ciphertext for RSA decryption.")
    else:
        # ... (كود فك التشفير باستخدام base64 كما هو) ...

# ... (باقي الكود الخاص بالواجهة كما هو) ...
