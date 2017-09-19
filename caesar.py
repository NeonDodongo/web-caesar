import string

def alphabet_position(letter):
    up_alpha = string.ascii_uppercase
    low_alpha = string.ascii_lowercase

    if letter in up_alpha:
        return up_alpha.find(letter)
    elif letter in low_alpha:
        return low_alpha.find(letter)

def rotate_character(char, rot):
    original_pos = alphabet_position(char)
    new_pos = original_pos + rot

    if new_pos >= 26:
        new_pos = new_pos % 26

    if char in string.ascii_lowercase:
        return string.ascii_lowercase[new_pos]
    elif char in string.ascii_uppercase:
        return string.ascii_uppercase[new_pos]
    else:
        return char

def encrypt_string(text, rot):
    new_text = ""
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text
