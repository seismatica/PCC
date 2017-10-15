def return_matched_strings(key_str, target_str):
    """
    Return potential (not exhaustive) matched substrings between 2 strings
    :param key_str: Shorter string where fragments are generated and looked up in the target string
    :param target_str: Longer string in which the key string fragments are looked up against
    :return: List of potential matched substrings that will include the longest match
    """
    matched_strings = []
    # Fragments start from 0 and get successively smaller (by incrementing the starting index)
    for start in range(len(key_str)):
        # For each start position, end of fragments start from end of string and get successively smaller
        # (by decreasing the ending index)
        for end in range(len(key_str), start, -1):
            # Check if a key string fragment of certain start and end points appear in the target string.
            # If so, do not check smaller strings at that given start point (by changing the end point),
            # but move to the next start point.
            str_fragment = key_str[start:end]
            if str_fragment in target_str:
                matched_strings.append(str_fragment)

                break
    return matched_strings


def lcs(str1, str2):
    """
    Find longest common substrings between 2 strings
    :param str1: first string
    :param str2: second string
    :return: list of longest common substring(s) between 2 strings
    """

    # Assign short string as key string, and longer string as target string
    if len(str1) <= len(str2):
        key_str = str1
        target_str = str2
    else:
        key_str = str2
        target_str = str1

    # Get list of matched substrings between key and target string
    matched_substrings = return_matched_strings(key_str, target_str)

    # Get the maximum length of the matched substrings
    max_length = max(len(string) for string in matched_substrings)

    # Collect the matched substrings with the highest length
    longest_substrings = [string for string in matched_substrings if len(string) == max_length]

    return longest_substrings


if __name__ == '__main__':
    str1 = 'function'
    str2 = 'functioqzunction'
    print(lcs(str1, str2))