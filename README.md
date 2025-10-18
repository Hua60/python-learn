# python-learn
python学习过程中的一些代码

## Python知识点总结

### 02_Python入门语法
- **字面量**: 在代码中直接写出的数据。
  ```python
  print(666)
  print(13.14)
  print("黑马程序员")
  ```
- **注释**: 对代码的解释说明，不被执行。
  ```python
  # 这是单行注释
  """
  这是多行注释
  """
  ```
- **变量**: 用来存储数据的容器。
  ```python
  money = 50
  money = money - 10
  ```
- **数据类型及转换**:
  ```python
  # 字符串转整数
  num = int('11') 
  # 整数转字符串
  num_str = str(11)
  ```
- **标识符**: 变量、函数、类等的名字，需要遵循命名规则。
- **运算符**: 用于执行数学或逻辑运算。
- **字符串（定义、拼接、格式化）**:
  ```python
  name = "黑马程序员"
  message = "学IT来：%s" % name
  print(message)
  ```
- **数据输入（`input`函数）**:
  ```python
  name = input("请输入：")
  print("我知道了，你是%s" % name)
  ```

### 03_Python判断语句
- **布尔类型和比较运算符**: `True` 和 `False`。
- **`if`语句**:
  ```python
  if 10 >= 18:
      print("我已经成年了")
  ```
- **`if-else`语句**:
  ```python
  if 10 >= 18:
      print("我已经成年了")
  else:
      print("我还未成年")
  ```
- **`if-elif-else`语句**:
  ```python
  if age < 120:
      print("免费")
  elif vip_level > 3:
      print("免费")
  else:
      print("买票10元")
  ```
- **判断语句的嵌套**:
  ```python
  if age >= 18:
      if year > 2:
          print("可以领取礼物")
  ```

### 04_Python循环语句
- **`while`循环**:
  ```python
  i = 0
  while i < 100:
      print("小美，我喜欢你")
      i += 1
  ```
- **`for`循环**:
  ```python
  name = "itheima"
  for x in name:
      print(x)
  ```
- **`range`语句**: 生成一个整数序列。
  ```python
  for i in range(5):
      print(i)
  ```
- **循环嵌套**:
  ```python
  for i in range(3):
      for j in range(2):
          print("i=%d, j=%d" % (i, j))
  ```
- **`break`和`continue`**: `break` 退出循环, `continue` 跳过本次循环。
  ```python
  for i in range(1, 6):
      print("语句1")
      continue
      print("语句2") # 这句不会被执行
  ```
- **变量作用域**: 变量在程序中可用的范围。

### 05_函数
- **函数的定义和调用**:
  ```python
  def say_hi():
      print("Hi 我是黑马程序员")
  say_hi()
  ```
- **函数的参数和返回值**:
  ```python
  def add(x, y):
      return x + y
  r = add(5, 6)
  ```
- **函数的说明文档**:
  ```python
  def add(x, y):
      """
      这个函数用于计算两个数的和
      :param x: 第一个数
      :param y: 第二个数
      :return: 两个数的和
      """
      return x + y
  ```
- **函数的嵌套调用**:
  ```python
  def foo():
      print("Hello")
  def bar():
      foo()
  bar()
  ```
- **变量在函数中的作用域**:
  ```python
  x = 10
  def func():
      x = 5
      print(x)
  func() # 输出5
  print(x) # 输出10
  ```

### 06_数据容器
- **`list`（列表）**: 可变的有序集合。
  ```python
  my_list = ["itheima", "itcast", "python"]
  print(my_list[0])
  ```
- **`tuple`（元组）**: 不可变的有序集合。
  ```python
  t1 = (1, "Hello", True)
  ```
- **`str`（字符串）**:
- **序列切片**:
  ```python
  my_list = [0, 1, 2, 3, 4, 5]
  print(my_list[1:4]) # 输出 [1, 2, 3]
  ```
- **`set`（集合）**: 无序、不重复的元素集合。
  ```python
  my_set = {"传智教育", "黑马程序员", "itheima"}
  ```
- **`dict`（字典）**: 键值对的无序集合。
  ```python
  my_dict1 = {"王力鸿": 99, "周杰轮": 88}
  score = my_dict1["王力鸿"]
  ```

### 07_函数进阶
- **多返回值**:
  ```python
  def test_return():
      return 1, "hello", True
  x, y, z = test_return()
  ```
- **多种参数使用形式**:
- **函数作为参数传递**:
- **`lambda`匿名函数**:
  ```python
  test_func(lambda x, y: x + y)
  ```

### 08_文件操作
- **文件读取**:
  ```python
  f = open("D:/测试.txt", "r", encoding="UTF-8")
  content = f.read()
  f.close()
  ```
- **文件写入**:
  ```python
  f = open("D:/test.txt", "w", encoding="UTF-8")
  f.write("Hello World!!!")
  f.close()
  ```
- **文件追加**:
  ```python
  f = open("D:/test.txt", "a", encoding="UTF-8")
  f.write("Hello Again!!!")
  f.close()
  ```

### 09_异常_模块_包
- **异常捕获**:
  ```python
  try:
      f = open("D:/abc.txt", "r")
  except:
      print("出现异常了")
  ```
- **模块的导入**:
  ```python
  import time
  time.sleep(5)
  
  from time import sleep
  sleep(5)
  ```
- **自定义模块和包**:

### 10_可视化案例
- **JSON数据格式**:
- **`pyecharts`库入门**:
  ```python
  from pyecharts.charts import Line
  line = Line()
  line.add_xaxis(["中国", "美国", "英国"])
  line.add_yaxis("GDP", [30, 20, 10])
  line.render()
  ```
- **折线图**:
- **地图**:
- **柱状图**:
- **动态柱状图**:
