import time
localtime = time.localtime()
print("Local time is: ",localtime)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print("formatted time is: ",formatted_time)