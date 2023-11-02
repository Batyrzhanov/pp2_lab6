from datetime 
import datetime

datewithmicroseconds = datetime.now()

datewithoutmicroseconds = datewithmicroseconds.replace(microsecond=0)

print(datewithmicroseconds)
print(datewithoutmicroseconds)