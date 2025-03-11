def rot_decrypt(ciphertext):
    """
    Brute force a ROT cipher by trying all 26 possible rotations.

    :param ciphertext: The encoded string to be decrypted.
    """
    for shift in range(26):
        decrypted_text = ""
        for char in ciphertext:
            # Check if the character is an uppercase letter
            if 'A' <= char <= 'Z':
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # Check if the character is a lowercase letter
            elif 'a' <= char <= 'z':
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                # Non-alphabetic characters remain unchanged
                decrypted_text += char
        print(f"ROT-{shift}: {decrypted_text}")


if __name__ == "__main__":
    # Example ciphertext encoded with a ROT cipher
    ciphertext = "xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}"
    print(f"Ciphertext: {ciphertext}\n")
    print("Attempting to decrypt using brute-force:\n")
    rot_decrypt(ciphertext)
