def line_input(message: str = "", mode: str = "", min_char_len: int = 0, max_char_len: int = 0) -> str:
    ''' function to validate line input
        mode : "alpha" > just characters
        mode : "nun" > just numbers
        mode : "numalpha" or "alphanum" > accepts both
    '''
    if min_char_len <= 0:
        min_char_len = 0
        min_char_len_check = True
    else:
        min_char_len_check = False
    if max_char_len <= 0:
        max_char_len = 0
        man_char_len_check = True
    else:
        if max_char_len < min_char_len:
            max_char_len = min_char_len + 1
        man_char_len_check = False

    done = False
    strict = False
    mode = mode.lower()
    while not done:
        line_input_result = input(message)
        if line_input_result != "" and mode != "":
            if "!" in mode:
                strict = True            
            if ("alpha" in mode and not "num" in mode):
                if line_input_result.isalpha():
                    done = True
            if ("num" in mode and not "alpha" in mode):
                if line_input_result.isnumeric():
                    done = True
            if "alpha" in mode and "num" in mode:
                if line_input_result.isalnum():
                    if strict:
                        if (not line_input_result.isalpha()) and (not line_input_result.isnumeric()):
                            done = True
                    else:
                        done = True
        else:
            done = True

        if done and (min_char_len != 0 or max_char_len != 0):
            done = False
            if min_char_len and len(line_input_result) >= min_char_len:
                min_char_len_check = True
            if max_char_len and len(line_input_result) <= max_char_len:
                man_char_len_check = True
            if min_char_len_check and man_char_len_check:
                done = True

    return line_input_result


res = line_input(message = "Input : ", mode = "alpha", min_char_len = 0, max_char_len = 5)
print(res)