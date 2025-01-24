from random import choice

# 可选的号码池
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

# 初始化循环控制变量
lottery_roll_number = 0
lottery_active = True

while lottery_active:
    # 每次开始新循环时重置列表
    my_lottery = []
    win_numbers = ['1', '2', 'a', 'b']
    
    # 记录循环次数
    lottery_roll_number += 1
    print(f"Attempt #{lottery_roll_number}")

    # 生成4个随机字符
    while len(my_lottery) < 4:
        lottery_word = choice(lottery)
        my_lottery.append(lottery_word)

    # 检查匹配并删除匹配项
    for item in my_lottery[:]:  # 使用列表副本来迭代避免修改时出错
        if item in win_numbers:
            win_numbers.remove(item)

    # 如果所有中奖号码都匹配并被删除，则中奖
    if not win_numbers:
        lottery_active = False

print(f"Congratulations! You won after {lottery_roll_number} attempts!")