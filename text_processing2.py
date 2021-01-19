def digits_to_words(input_string):
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    digit_string = ""
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            idx = int(input_string[i])
            digit_string += (numbers[idx] + " ")
    return digit_string[:-1]

def to_camel_case(underscore_str):
    if underscore_str.find('_') == -1: return underscore_str
    camelcase_str  = ""
    first = False #첫글자가 대문자면 True
    for i in underscore_str:
        if i == '_':
            first = True
        else:
            if first:
                camelcase_str += i.upper()
                first = False
            else:
                camelcase_str += i.lower()
    if not len(camelcase_str): return ""
    return camelcase_str[0].lower() + camelcase_str[1:]

'''
def main():
    tmp = input()
    print(to_camel_case(tmp))

main()
'''
