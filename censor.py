import lists

def ireplace(data, prev_pattern, new_pattern):
    """
        Replaces words while ignoring letters case.
    """

    # find the index of the pattern which is going to be replaced
    idx = data.lower().find(prev_pattern.lower())

    # replaces the founded pattern with a new specified pattern
    mod_data = data.replace( 
        data[idx:idx+len(prev_pattern)], new_pattern)
    return mod_data


def censor(msg):
    """
        Censors the message according to given patterns.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for pattern in lists.CENSORED:
        if pattern in msg.lower():
            idx = msg.lower().find(pattern)
            rev_data = msg[idx:idx+len(pattern)]
            for char in rev_data:
                for v in vowels:
                    if char == v:
                        # to send asterisk in discord, you gotta use backslash asterisk (\*)
                        rev_data = rev_data.replace(char, '\*') 
            msg = ireplace(msg, pattern, rev_data)
    return msg

