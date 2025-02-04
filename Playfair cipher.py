def generate_matrix(key):
    key = key.upper().replace("J", "I") 
    key = "".join(dict.fromkeys(key))  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix = [c for c in key if c in alphabet]  

    for c in alphabet:
        if c not in matrix:
            matrix.append(c) 
    return [matrix[i:i + 5] for i in range(0, 25, 5)]  
def get_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def pt(text):
    text = text.upper().replace("J", "I").replace(" ", "")  
    prepared = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'  
        if a == b:
            prepared.append((a, 'X')) 
            i += 1
        else:
            prepared.append((a, b))
            i += 2
    return prepared

def encrypt(plaintext, key):
    matrix = generate_matrix(key)
    pairs = pt(plaintext)
    encrypted = ""

    for a, b in pairs:
        r1, c1 = get_position(matrix, a)
        r2, c2 = get_position(matrix, b)
        if r1 == r2:  
            encrypted += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  
            encrypted += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else: 
            encrypted += matrix[r1][c2] + matrix[r2][c1]
    
    return encrypted

def decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    pairs = pt(ciphertext)
    decrypted = ""

    for a, b in pairs:
        r1, c1 = get_position(matrix, a)
        r2, c2 = get_position(matrix, b)
        if r1 == r2:  # Same row
            decrypted += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Same column
            decrypted += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:  # Rectangle
            decrypted += matrix[r1][c2] + matrix[r2][c1]
    
    return decrypted

# Hardcoded key and plaintext
key = "monarchy"
plaintext = "intruments"
print("Key:", key)
print("Plaintext:", plaintext)
# Encrypting the plaintext
ciphertext = encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

# Decrypting the ciphertext
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)