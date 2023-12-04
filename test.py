from datetime import datetime

today = str(datetime.now())
print(today)
formatted_str = datetime.strptime(today, "%Y-%m-%d %H:%M:%S.%f")
print(formatted_str)

print()
print()

today = datetime.now()

# Convert the datetime object to a string in ISO 8601 format
today = today.isoformat()

print(today)