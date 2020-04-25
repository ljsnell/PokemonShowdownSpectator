def getNames(loaded_text):
    split_text = loaded_text.split("\n")
    left_name = split_text[1].replace(' joined.', '').replace('☆', '')
    right_name = split_text[2].replace(' joined.', '').replace('☆', '')
    return left_name, right_name