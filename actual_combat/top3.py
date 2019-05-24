"""尽量用一行代码统计中字符串中重复出现的字符（大小写敏感）,要求输出格式{字符：字符出现的次数}
输入：str1='AIDlkdiDKIiLLLLLdli'
输出：{'I': 2, 'D': 2, 'l': 2, 'd': 2, 'i': 3, 'L': 5}

# Tips:可以把[]替换成{}"""
count = {}
for character in 'AIDlkdiDKIiLLLLLdli':
	# setdefault方法调用确保了键存在于 count 字典中(默认值是 0),再次走到这里赋值为0是不会成功的
    count.setdefault(character, 0)
    count[character] += 1
print(count)











# print({count,(count.setdefault(character,0),count[character]+= 1, for character in 'AIDlkdiDKIiLLLLLdli')})