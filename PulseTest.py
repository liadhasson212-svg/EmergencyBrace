from machine import Pin, I2C
import time

# הגדרה של פין קריאת הפולס מהסנסור
pulse_pin = Pin(4, Pin.IN)

pulse_count = 0
last_state = 0
time_window = 15  # משך מדידה בשניות
start_time = time.ticks_ms()

while True:
    current_state = pulse_pin.value()
    # זיהוי קצה עולה של הפולס
    if current_state == 1 and last_state == 0:
        pulse_count += 1
    last_state = current_state

    elapsed = (time.ticks_ms() - start_time) / 1000
    if elapsed >= time_window:
        bpm = (pulse_count / time_window) * 60  # חישוב פעימות לדקה
        print("Pulse:", bpm)

          # איפוס המדידה לריצה נוספת
        pulse_count = 0
        start_time = time.ticks_ms()

    time.sleep_ms(10)