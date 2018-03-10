IDDLE_DATA = 0
SENSOR_TRESHOLD = 2

seq_count = 0
last_seq_count = 0

def process_sensor_data(data):
    global seq_count
    global last_seq_count

    if data == IDDLE_DATA:
        if seq_count > 0 and seq_count > SENSOR_TRESHOLD:
            last_seq_count = seq_count
        seq_count = 0
        return
    seq_count += 1


def replay_sensor_readings(param):
    global seq_count
    global last_seq_count

    seq_count = 0
    last_seq_count = 0

    for i in param:
        process_sensor_data(i)

    return last_seq_count
