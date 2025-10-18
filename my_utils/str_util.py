def str_reverse(s):
    """
    字符串反转
    :param s:
    :return:反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    字符串截取
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员", 1, 3))