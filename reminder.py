import time
import os

def reminder():
    interval_minutes = 30
    while True:
      
        current_time = time.strftime('%H:%M:%S')
    
        print(f"It's {current_time}. Time to drink water!")
        
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    reminder()
