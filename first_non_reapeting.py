from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

if __name__ == "__main__":
    print(first_non_repeating_char("swiss"))   