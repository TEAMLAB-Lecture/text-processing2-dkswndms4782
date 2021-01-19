def digits_to_words(input_string):
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    digit_string = ""
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            idx = int(input_string[i])
            digit_string += (numbers[idx] + " ")
    return digit_string

def to_camel_case(underscore_str):
    camelcase_str  = ""
    first = False #첫글자가 대문자면 True
    for i in underscore_str:
        if i.isalpha():
            if first:
                camelcase_str += i.upper()
                first = False
            else:
                camelcase_str += i.lower()
        else:
            first = True
    if not len(camelcase_str): return ""
    return camelcase_str[0].lower() + camelcase_str[1:]


