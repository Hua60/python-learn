def print_file_info(file_path):
    try:
        f = open(file_path, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("指定的文件不存在")
    except Exception as e:
        print(f"未知异常{e}")


def append_to_file(file_path, content):
    try:
        f = open(file_path, "a")
        f.write(content)
        f.write("\n")
        f.close()
    except Exception as e:
        print(f"未知异常{e}")

if __name__ == '__main__':
    # print_file_info("D:/bill.txt")
    append_to_file("D:/test_append.txt", "itheima")