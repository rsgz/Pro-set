import time,random,datetime
from datetime import datetime, timedelta, timezone

class Time:
    def __init__(self):
        pass

    def get_current_date_xingqi(self):
        r"""
        返回当前 日期 星期几
        """
        # 获取带有时区信息的当前时间（UTC -> 本地时区）
        current_time = datetime.now(timezone.utc).astimezone()

        # 格式化成日期字符串
        date_str = current_time.strftime("%Y-%m-%d")

        # 中文星期映射表
        weekdays = ["星期一", "星期二", "星期三", "星期四",
                    "星期五", "星期六", "星期日"]

        # 获取中文星期（isoweekday()返回1-7对应周一到周日）
        weekday = weekdays[current_time.isoweekday() - 1]

        return f"{date_str} {weekday}"

    def get_current_date_time(self):
        r"""
        返回当前日期时间
        """
        now = int(time.time())  # 获得当前时间时间戳
        timeArray = time.localtime(now)  # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        # print(otherStyleTime)  # 2025-01-25 11:28:30
        return otherStyleTime

    def get_current_time(self):
        r"""
        返回当前时间
        """
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def get_current_date(self):
        r"""
        返回当前日期
        """
        now = datetime.now()
        return now.strftime("%Y-%m-%d")

    def get_random_date_time(self):
        r"""
        返回随机 日期 时间
        """
        # 方法一：随机时间戳
        random_ts = random.randint(0, int(time.time()))
        dt = datetime.fromtimestamp(random_ts, tz=timezone.utc).astimezone()
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def get_random_date(self):
        r"""
        返回随机 日期
        """
        # 方法一：随机时间戳
        random_ts = random.randint(0, int(time.time()))
        dt = datetime.fromtimestamp(random_ts, tz=timezone.utc).astimezone()
        return dt.strftime("%Y-%m-%d")

    def get_random_time(self):
        r"""
        返回随机 时间
        """
        # 方法一：随机时间戳
        random_ts = random.randint(0, int(time.time()))
        dt = datetime.fromtimestamp(random_ts, tz=timezone.utc).astimezone()
        return dt.strftime("%H:%M:%S")


    def add_days(self, n):
        r"""
        返回n天后的时间
        """
        now = datetime.now()
        future = now + timedelta(days=n)
        return future.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    t=Time().get_current_date_xingqi()
    print(t)