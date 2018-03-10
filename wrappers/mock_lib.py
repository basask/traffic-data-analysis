IDDLE_DATA = 0
FALSE_NEGATIVE_TOLERANCE = 0
FALSE_POSITIVE_TOLERANCE = 2

seq_count = 0
fn_count = 0

def process_sensor_data(data):
    global seq_count
    global fn_count

    if data == IDDLE_DATA:
        if fn_count >= FALSE_NEGATIVE_TOLERANCE:
            fn_count = 0
            ret = seq_count if seq_count > FALSE_POSITIVE_TOLERANCE else 0
            seq_count = 0
            return ret
    seq_count += 1
    return 0


def replay_sensor_readings(param):
    global seq_count
    global fn_count

    seq_count = 0
    fn_count = 0

    ret = 0
    for i in param:
        res = process_sensor_data(i)
        ret = res if res > 0 else ret
    return ret
