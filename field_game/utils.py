from .data import *


async def is_admin(username):
    for user in admins:
        if user["username"] == username:
            return user
    
    return False

def check_code(code=""):
    if code in codes:
        if code[5:8] == 'win':
            codes.remove(code)
            return 100
        codes.remove(code)
        return int(code[4])
    else:
        return 404

def changer (ans, length):
    try:
        temp = list(ans.strip())
        if len(temp) != length:
            return False
        return temp
    except:
        return False

def unique(lis, length):
    return len(lis) == len(set(lis)) and len(lis) == length

def check_ans(user_ans, correct_ans):
    position = 0
    ans = changer(user_ans, len(user_ans))

    if not (ans) or not unique(ans):
        return wrong_msg
    
    for i in range(len(correct_ans)):
        if ans[i] == correct_ans[i]:
            position += 1
    
    if position == len(user_ans):
        return "correct"
    
    return f"{position}"

