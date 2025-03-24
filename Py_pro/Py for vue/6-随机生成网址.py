import random
import string

def generate_random_url(length=20):
    """生成随机的“伪”网址。"""
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars) for _ in range(length))
    # return f"https://www.random-{random_string}.com/{random_string}"
    return f"https://www.random-{random_string}.com/"

for _ in range(300):
    print(generate_random_url())