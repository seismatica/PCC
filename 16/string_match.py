from difflib import SequenceMatcher


def match(str1, str2):
    matched = SequenceMatcher(isjunk=lambda x: x in " ", a=str1.lower(), b=str2.lower())
    pos1, pos2, size = matched.find_longest_match(0, len(str1), 0, len(str2))
    matched_string = str1[pos1:pos1+size]
    return matched_string


if __name__ == "__main__":
    match("Viet Nam", "Vietnam")