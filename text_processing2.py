def digits_to_words(input_string):
    # numbers[0] = zero, numbers[8] = eight
    # 인덱스를 이용하여 문자변환 가능
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    digit_string = ""
    # 문자열 처음부터 끝까지 비교, 숫자라면 numbers[i]를 string에 더해준다.
    for i in range(len(input_string)):
        # isdigit()로 숫자인지 확인. return type : Boolean
        if input_string[i].isdigit():
            idx = int(input_string[i])
            digit_string += numbers[idx] + " "
    # string의 마지막이 " "일 것이므로 [:-1]슬라이싱 추가
    return digit_string[:-1]


def to_camel_case(underscore_str):
    # "alreadyCamel"같은 경우 예외처리. "_"가 없으면 CamelCase의 경우로 알고 바로 출력해준다.
    # find()로 "_"가 있는지 확인. return type : (-1 = 없는경우) (숫자 = 문자의위치)
    if underscore_str.find("_") == -1:
        return underscore_str
    camelcase_str = ""
    # 첫글자가 대문자면 True
    first = False
    # 문자열 처음부터 끝까지 확인.
    for i in underscore_str:
        # "_"가 있으면 first를 True로 설정해서 다음 문자의 첫글자를 대문자로 설정
        if i == "_":
            first = True
        else:
            # first가 True라서 Upper()를 사용해 대문자 더하기 해줌
            if first:
                camelcase_str += i.upper()
                # 다음문자들은 소문자가 되어야하기 때문에 first = False
                first = False
            else:
                camelcase_str += i.lower()
    # "           "같은 경우 예외처리
    if not len(camelcase_str):
        return ""
    # "__To_CAMEL" 같은 경우 camelcase_str은 ToCamel이 된다. 이와같은 경우 방지
    return camelcase_str[0].lower() + camelcase_str[1:]
