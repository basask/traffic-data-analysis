#include <stdlib.h>
#include <string.h>

#define IDDLE_DATA 0

// Sensor readings bellow this threshold shoul be discarted
#define SENSOR_TRESHOLD 2

// Accumulate positive sensor readings streak
int seq_count;

// Store last valid sensor detection
int last_seq_count;


/*
    Process the sensor readings in sequence identifying radings streaks
*/
void process_sensor_data(int data) {
    if (data == IDDLE_DATA) {
        if(seq_count > 0 && seq_count > SENSOR_TRESHOLD){
            last_seq_count = seq_count;
        }
        seq_count = 0;
        return;
    }
    seq_count += 1;
}

extern "C" {
    /*
        This function parses an sensor_stream (char *) in the csv format into a list of integers.
        Then it feeds this integers in sequence into process_sensor_data function
        to emulate data sequencing comming from real sensors.
    */
    int replay_sensor_readings(char *sensor_stream) {

        seq_count = 0;
        last_seq_count = 0;

        const char *tok;
        int sensor_data = 0;

        strtok(sensor_stream, ",");
        while((tok = strtok(NULL, ","))) {
            sensor_data = atoi(tok);
            process_sensor_data(sensor_data);
        }
        return last_seq_count;
    }
}