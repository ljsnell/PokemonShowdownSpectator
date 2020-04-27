import re

def getNames(loaded_text):
    split_text = loaded_text.split("\n")
    left_name = getCleanString(split_text[1].replace(' joined.', '').replace('☆', ''))
    
    right_name = getCleanString(split_text[2].replace(' joined.', '').replace('☆', ''))
    return left_name, right_name

def getWinner(bodyText):
    matched_lines = [line for line in bodyText.split('\n') if " won " in line]
    # Find first part and return slice before it.
    pos_a = matched_lines[0].find(' won ')
    winner = getCleanString(matched_lines[0][0:pos_a])
    return winner
    
def getCleanString(string2Clean):
    return re.sub(r'\W+', '', string2Clean)
