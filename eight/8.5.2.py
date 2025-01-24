def build_profile(frist,last,**user_info):
    """创建一个字典,其中憨憨我们知道的有关用户的一切"""
    user_info['frist_name']=frist
    user_info['last_name']=last
    return user_info
user_profile=build_profile('arch','jiang',location='chifeng',field='physics')

print(user_profile)