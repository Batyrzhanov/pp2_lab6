from datetime 
import datetime

d1 = datetime(2023, 10, 19, 17, 17, 30)
d2 = datetime(2023, 10, 19, 17, 17, 10)

time_difference = (d2 - d1).total_seconds()

print(abs(time_difference))
