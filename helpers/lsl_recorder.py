"""
LSLRecorder is a thread-based class for recording Lab Streaming Layer (LSL) data streams to CSV files.

This class handles the continuous recording of data from an LSL inlet, including:
- Automatic channel label detection from stream metadata
- Timestamped data collection with marker support
- Buffered CSV file writing with configurable markers
- Thread-safe operation for concurrent data recording

The recorder creates CSV files with headers including timestamp, channel data, and markers,
making it suitable for recording various types of streaming data like EEG, eye tracking,
or other sensor data with synchronization markers.
"""

import csv
import time
import threading
import xmltodict


class LSLRecorder(threading.Thread):
    def __init__(self, inlet, csv_file_name):
        super().__init__()
        self.inlet = inlet

        self.csv_file_name = csv_file_name

        # Get channel information
        meta_data = xmltodict.parse(inlet.info().as_xml())
        channels = []
        if 'desc' in meta_data['info']:
            if meta_data['info']['desc'] is not None:
                if 'channels' in meta_data['info']['desc']:
                    ch = meta_data['info']['desc']['channels']['channel']
                    channels = [c['label'] for c in ch]

        if len(channels) <= 0:
            channels = [f"Channel_{i + 1}" for i in range(inlet.info().channel_count())]

        self.headers = ["Timestamp"] + channels + ["Marker"]

        self.marker = -1
        self.running = True

    def run(self):
        # Initialize a buffer
        buffer = []

        with open(self.csv_file_name, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(self.headers)  # Write the headers

            print("Receiving data and writing to CSV...")

            while self.running:
                chunk, timestamps = self.inlet.pull_chunk()
                if timestamps:
                    for i in range(len(timestamps)):
                        buffer.append([timestamps[i]] + chunk[i] + [self.marker])

                    writer.writerows(buffer)
                    buffer.clear()  # Clear the buffer after writing

                time.sleep(0.1)

            if buffer:
                writer.writerows(buffer)

            print(f"Data collection stopped. CSV file saved as {self.csv_file_name}.")

    def end_run(self):
        self.running = False
        self.inlet.close_stream()

    def change_marker(self, marker):
        self.marker = marker
