# names = ['xiaomeng','xiaoming']
# for name in names:
#     if  name == 'xiao':
#         print('名称:',name)
#         break
#     print('循环名称列表' + name)
# else:
#         print('没有循环数据')
# print('循环结束')
# name = 'xiaomeng'
# if name == 'xiaomeng':
#     print('Hello')
# elif name == 'xiaomeng':
#     #不做任何处理
#     pass
# else:
#     print('nothing')

# num = 10
# for nums in range(11):
#     if nums > 8:
#         print('当前的数字是：',nums)
#     else:
#         continue
#
# number = 10
# while number > 0:
#     print('当前的数字是：', number)
#     number-=1
#     if number == 8:
#         break
#
for nums in range(1000):
    if 0 < nums < 10:
        if nums**1 == nums:
            print(nums)
            continue
    elif  10 <= nums <= 99:
        if int(nums / 10)**2 + (nums % 10)**2 == nums:
            print(nums)
            continue
    elif 100 <= nums <= 1000:
        if int(nums / 100)**3 + int((nums % 100)/10)**3 +int((nums % 100)%10)**3 == nums:
            print(nums)
            continue
# 153

#
# nums = 153
# print(int((nums % 100)%10))
#
# print(int(nums / 100)**3 + int((nums % 100)/10)**3 +int((nums % 100)%10)**3)
# nums = 153
# print(int((nums % 100)%10))
#
# print(int(nums / 100)**3 + int((nums % 100)/10)**3 +int((nums % 100)%10)**3)