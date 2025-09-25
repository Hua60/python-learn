# 方式一 使用print直接输出类型信息
print(type(666))
print(type(13.14))
print(type("黑马程序员"))

# 方式二 使用变量存储type()语句的结果
string_type = type("黑马程序员")
print(string_type)

# 方式三 使用type语句，查看变量中存储的数据类型信息
name = "黑马程序员"
type_name = type(name)
print(type_name)