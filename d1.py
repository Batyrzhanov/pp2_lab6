from datetime  
import datetime, timedelta

c_date = datetime.now()
fivedaysago = c_date - timedelta(days=5)
print(c_date)
print(fivedaysago)
