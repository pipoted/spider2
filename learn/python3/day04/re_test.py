# coding=utf-8

import re


# 匹配某个字符串
# text = 'hello'
# ret = re.match('he', text) # 只能从最开始的字符开始匹配 
# print(ret.group())

# . 匹配一个任意字符, 但是无法匹配换行符
# text = 'hello'
# ret = re.match('.', text)
# print(ret.group())

# \d 匹配任意的数字(0~9), 同时\D匹配任意的非数字
# text = '12hello'
# ret = re.match('\d', text)
# print(ret.group())

# \s 匹配空白字符(\n, \t, \r, 空格)
# text = ' hello'
# ret = re.match('\s', text)
# print(ret.group())

# \w 匹配任意字母数字下划线, \W相反
# text = '_a'
# ret = re.match('\w', text)
# print(ret.group())

# [] 组合的方式进行匹配， 只要满足括号中的要求就能够进行匹配
# text = '1hello'
# ret = re.match('[h1]', text)
# print(ret.group())
# text = '0796-8888888888888'
# ret = re.match('[\d\-]+', text) # + 至少匹配一次目标表达式
# print(ret.group())
# 可以使用-表达一个范围（0-9 a-z A-Z）, 同时可以使用^字符表示非
# text = '8'
# ret = re.match('[0-9]', text)
# print(ret.group())

# --------------------------
# 匹配多个字符
# * 可以匹配目标表达式0到任意多次
# text = 'a199110'
# ret = re.match('(\d)*', text)
# print(ret.group())

# ? 匹配一次或者0次

# {m} 匹配m次
# text = 'abcd'
# ret = re.match('\w{3}', text)
# print(ret.group())

# {m, n} 匹配m到n次, 但是会尽可能多的进行匹配


#################################### 案例

# 验证手机号码
# text = '15570136250'
# ret = re.match('1[34578]\d{9}', text)
# print(ret.group())

# 验证邮箱
# text = '1257397583_@qq.com'
# ret = re.match('[1-9a-zA-Z]\w+@[a-z]+\.com', text)
# print(ret.group())

# 验证url
# text = 'http://www.baidu.com'
# ret = re.match('(http|https|ftp)://[^\s]+', text)
# print(ret.group())

# 验证身份证号码
# text = '36242219970208001x'
# ret = re.match('\d{17}[\dxX]', text)
# print(ret.group())


# ^ 以匹配字符串开头
# text = 'hello'
# ret = re.match('^h', text)
# print(ret.group())

# $ 匹配目标表达式结尾
# text = 'hello'
# ret = re.match('(.+)o$', text)
# print(ret.group())

# | 多个条件进行选择
# text = 'hello'
# ret = re.match('hello|world', text)
# print(ret.group())

# 贪婪模式会尽可能多的进行匹配，直到不匹配位置
# 非贪婪模式只会最对进行一次匹配, 对目标表达式加？可达到该效果

# 案例 匹配0-100的数字
text = '1001'
ret = re.match('[1-9]\d?$|100$', text)
print(ret.group())
