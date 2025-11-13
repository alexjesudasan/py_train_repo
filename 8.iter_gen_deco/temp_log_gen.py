import random
import time
from datetime import datetime

def sensor_data_stream():
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        timenow=datetime.now()
        timestamp = timenow.strftime("%H:%M:%S")
        yield f"[{timestamp}] Temperature:{temperature}°C"
        time.sleep(1)  # simulate delay between readings


# Example: consume the generator
# for reading in sensor_data_stream():
#     print(reading)

read=sensor_data_stream()
itr_gen=iter(read)
print(next(itr_gen))
print(next(itr_gen))


