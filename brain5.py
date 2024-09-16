import languagemodels as lm
from db_operations import find_section_info

def ReplyBrain(input):
    lm.config["max_ram"] = "4gb"
    
    if "section" in input:
        section_number = extract_section_number(input)
        
        section_info = find_section_info(section_number)
        return section_info
    else:
        output = lm.do(input)
        return output

def extract_section_number(input):
    words = input.split()
    for word in words:
        if word.isdigit():  
            return int(word)
    return None
