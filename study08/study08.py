#字典学习记录



#创建
Members = {
    'account1' : 12,
    'account2' : 23,
    'account3' : 34,
    'account4' : 45
}
#print(Members)


#访问
#print("Members['account2'] = " , Members['account2'])


#增加\修改
"""
Members['account1'] = 0
Members['account2'] = 'test'
Members['account5'] = 56
"""
#print(Members)


#删除
"""
var = Members.pop('account1')
del Members['account5']
print("var = " ,var)
print(Members)
"""


#判断存在
'''
if 'account1' in Members :
    print("account 1 in Members")
if 'account2' in Members :
    print("account 2 in Members")
'''


#遍历
"""
for index , value in Members.items() :
    print(f"{index} -> {value}")
"""


#获取键列表
"""
key = Members.keys()
print(f"keys = {key}")
print(f"type of keys = {type(key)}")
"""


#长度
"""
print(f"length of members = {len(Members)}")
"""

#清空
"""
print(Members)
Members.clear()
print(Members)
"""


#合并
"""
print(Members)
Members2 = {
    'account7' : 78,
    'account8' : 89,
}
Members.update(Members2)
print(Members)
"""


