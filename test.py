from datetime import datetime

today = str(datetime.now())
print(today)
formatted_str = datetime.strptime(today, "%Y-%m-%d %H:%M:%S.%f")
print(formatted_str)

