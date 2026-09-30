def start_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time.sleep(1)
    print("Timer finished!")