def get_num_words(text_input):
    x = text_input.split()
    return len(x)

def char_count(text_input):
    char_dict ={}
    for i in text_input:
        lower_val = i.lower()
        if lower_val in char_dict:
            char_dict[lower_val] += 1
        else:
            char_dict[lower_val] = 1
    return char_dict

def dict_report(input_dict):
    sorted_dict = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)   
    return sorted_dict
    