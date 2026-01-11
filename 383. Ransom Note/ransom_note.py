from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_letter_count = defaultdict(int)
    magazine_letter_count = defaultdict(int)

    for ch in ransomNote:
        ransom_letter_count[ch] += 1

    for ch in magazine:
        if ch in ransom_letter_count:
            magazine_letter_count[ch] += 1

    for key in ransom_letter_count:
        if magazine_letter_count[key] < ransom_letter_count[key]:
            return False

    return True