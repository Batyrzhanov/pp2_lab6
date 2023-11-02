from datetime 
import datetime, timedelta

c_date = datetime.now()
y = c_date - timedelta(days=1)
t = c_date + timedelta(days=1)

print(y)
print(c_date)
print(t)