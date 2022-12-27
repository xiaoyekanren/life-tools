# coding=utf-8
from random import choice
from random import choices
from random import shuffle
from sys import exit
from sys import argv

num = '1234567890'
word_small = 'abcdefghijklmnopqrstuvwxyz'.lower()
word_large = word_small.upper()
symbol = '~!@#$%^&*()-+_=,.'
pass_type_list = [num, word_small, word_large, symbol]
error_msg = "默认生成密码，长度12位，密码包含：数字、英文大写、英文小写、符号 \n 可选参数1：取值范围：7~+∞，指定密码长度 \n 可选参数2：取值范围：3-4，是否带符号，取值3不包含符号，取值4包含符号"


def check_pass_length(password):
    if password < 7:
        print(f'密码长度不能少于7位，当前为: {str(argv[1])}')
        exit()


def main(len_pass):
    avg_length = int(len_pass / len(pass_type_list))
    last_group_length = len_pass - avg_length * (len(pass_type_list) - 1)

    i = 0
    password = ''
    len_pass_type_list = len(pass_type_list)
    while i < (len_pass_type_list - 1):
        random_type = choice(pass_type_list)
        pass_type_list.remove(random_type)
        random_tmp_str = ''.join(choices(random_type, k=avg_length))
        password += random_tmp_str
        i += 1
    password += ''.join(choices(pass_type_list[0], k=last_group_length))
    list_passowrd = list(password)
    shuffle(list_passowrd)
    return ''.join(list_passowrd)


if __name__ == '__main__':
    len_para = len(argv)
    len_pass = 12
    if len_para == 1:
        print(error_msg)
        pass
    elif len_para == 2:
        len_pass = int(argv[1])
        check_pass_length(len_pass)
    elif len_para == 3:
        len_pass = int(argv[1])
        check_pass_length(len_pass)
        if int(argv[2]) == 3:
            pass_type_list.remove(symbol)
        elif int(argv[2]) == 4:
            pass
        else:
            print(f"可选参数2：取值范围：3-4，当前为: {str(argv[2])}")
            exit()
    else:
        print(error_msg)
        exit()
    print(main(len_pass))
    input("按任意键退出...")
