# -*- coding: utf-8 -*-
import re

def getNames(battle_log):
    "Extracts player usernames from loaded battle log"
    
    split_text = battle_log.split("\n")
    left_name = getCleanString(split_text[1].replace(' joined.', '').replace('☆', ''))
    right_name = getCleanString(split_text[2].replace(' joined.', '').replace('☆', ''))
    
    return left_name, right_name

def getWinner(battle_log, left_name, right_name):
    "Extracts username of battle winner from battle log"
    
    # in first line mentioning " won ", find first part and return slice before it
    matched_lines = [line for line in battle_log.split('\n') if " won " in line]
    pos_a = matched_lines[0].find(' won ')
    winner = getCleanString(matched_lines[0][0:pos_a])
    if winner.lower() == left_name.lower():
        return 'left'
    else:
        return 'right'

def getCleanString(string2Clean):
    "Removes characters that aren't alphanumeric or underscore"
    
    return re.sub(r'\W+', '', string2Clean)
