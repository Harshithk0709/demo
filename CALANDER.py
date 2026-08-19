
import datetime

now = datetime.datetime.now()

print(" D A Y  : ",now.strftime("%A"))
print(" M O N T H  : ",now.strftime("%B"))
print(" Y E A R  : ",now.strftime("%Y"))
print(" T I M E (12 HR FORMAT)  : ",now.strftime("%I:%M:%S %p"))
print(" T I M E (24 HR FORMAT)  : ",now.strftime("%H:%M:%S %p"))

