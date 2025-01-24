def get_formatted_name(first,last,middle=''):
    """生成格式规范的名称"""
    if middle:
        fullname=f"{first} {middle} {last}"
    else:
        fullname=f"{first} {last}"
    return fullname.title()