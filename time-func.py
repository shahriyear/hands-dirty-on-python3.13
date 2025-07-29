import time

print("time.time(): ", time.time())
time.sleep(3)
print("3 seconds passed")

print("time.ctime(): ", time.ctime())
print("time.gmtime(): ", time.gmtime())
print("time.localtime(): ", time.localtime())
print("time.strftime(): ", time.strftime("%Y-%m-%d %H:%M:%S"))
print("time.strptime(): ", time.strptime("2025-07-30 00:25:22", "%Y-%m-%d %H:%M:%S"))
print("time.perf_counter(): ", time.perf_counter())
print("time.process_time(): ", time.process_time())
print("time.timezone(): ", time.timezone)
