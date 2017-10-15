def get_matched_positions(key_string, target_string):
    """
    For each letter in key string, return a list of locations where that letter is found in the target string
    :param key_string: String whose letters are used as key for lookup
    :param target_string: String whose matched indices with letter from key string will be stored
    :return: List of items, each item is a list of positions where the key letter was found in the target string
    """
    matched_positions = []
    # For each letter in key string, find the matched positions of it in the target string
    for key_letter in key_string:
        matched_position = []
        for target_index, target_letter in enumerate(target_string):
            if target_letter == key_letter:
                matched_position.append(target_index)

        # Combine matched positions of all key string letters
        matched_positions.append(matched_position)

    return matched_positions


def get_longest_left(found_positions):
    """
    Find the longest key string length to the left of a given position in the target string
    :param found_positions: list of items, each a list of positions where the key letter was found in the target string
    :return: dict with target string position as key, longest key string length to the left of the
    target string position as value.
    Example: {10: 1, 15:3} means part of key string was found on position 10, and positions 13, 14, 15 of the target
    string
    """
    # Create a dict to store matched position, traversed index, and current length of the matched substring
    # For example, {9: {'length': 3, 'index': 7}} means a 3-character substring of [5(7+1-3) : 8(7+1)] of key string
    # was matched to positions [7(9+1-3) : 10(9+1)] of target string
    pos_ind_len = {}

    for key_index, found_positions in enumerate(found_positions):
        for position in found_positions:
            # Check another matched position was found immediately before the current matched position
            if position-1 in pos_ind_len:
                # Also check if this previously matched position was a character immediate before the current character
                # in key string (using key index). If both conditions satisfied, modify the dict entry with the
                # new position (+1) and new index (+1)
                previous_position = pos_ind_len[position - 1]
                if key_index-1 == previous_position['index']:
                    pos_ind_len[position] = {}
                    pos_ind_len[position]['length'] = previous_position['length'] + 1
                    pos_ind_len[position]['index'] = key_index

                    # Delete old matched position entry
                    del pos_ind_len[position-1]
                    # print("a.", key_index, found_positions, position, pos_ind_len)

            # If no position or no immediate previous position was found, create new position record with the current
            # key index and length (1)
            else:
                if position not in pos_ind_len:  # Ignore positions that have already been building
                    pos_ind_len[position] = {'index': key_index, 'length': 1}
                    # print("b.", key_index, found_positions, position, pos_ind_len)

    # Remove index information since it's no longer needed.
    # Return dict of end target position : string length of matched substrings
    for key, value in pos_ind_len.items():
        pos_ind_len[key] = value['length']

    return pos_ind_len


def find_longest_string(target_string, pos_ind_len):
    """
    Return the longest key string fraction found in the target string
    :param target_string: target string where the longest strings will be extracted from
    :param pos_ind_len: dict of position in target string and its longest leftward key string fragment
    :return: list of longest key strings found in the target string
    """
    longest_matched_strings = []
    max_length = max(pos_ind_len.values())
    for position, length in pos_ind_len.items():
        if length == max_length:
            longest_matched_string = target_string[position+1-length:position+1]
            longest_matched_strings.append(longest_matched_string)
    return longest_matched_strings


def return_longest_substrings(key_string, target_string):
    """
    Find longest substring of 2 given strings
    :param key_string: string used for lookup
    :param target_string: string onto which lookup is done
    :return: list of longest substrings between 2 strings
    """
    found_positions_by_index = get_matched_positions(key_string, target_string)
    # print(key_string, target_string, found_positions_by_index)
    current_length_at_position = get_longest_left(found_positions_by_index)
    longest_substrings = find_longest_string(target_string, current_length_at_position)
    return longest_substrings


if __name__ == '__main__':
    target_string = "function"
    key_string = "functionzqunction"
    longest_substrings = return_longest_substrings(key_string, target_string)
    print(longest_substrings)