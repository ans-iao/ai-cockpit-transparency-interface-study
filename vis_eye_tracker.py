"""
Real-time Eye Tracking Visualization Script

This script visualizes eye tracking data received through Lab Streaming Layer (LSL).
It creates a simple visual representation of the user's gaze point on a canvas
in real-time.

The script:
- Connects to an eye tracking LSL stream
- Processes incoming gaze coordinates
- Displays gaze points as circles on a visualization window
- Uses a buffer to smooth gaze point movement
- Runs at 30 FPS

Dependencies:
- numpy: For numerical operations
- pylsl: For LSL stream handling
- opencv-python (cv2): For visualization
- config: Local configuration file with window dimensions and LSL settings

Usage:
Run the script to start visualization. Press 'q' or close the window to exit.
"""

import numpy as np
from pylsl import StreamInlet, resolve_byprop
import config as cfg
import cv2
import math
import time
from collections import deque

# Setup LSL eye-tracking stream
print(f"Looking for an eye-tracking stream...")
streams = []
tries = 1
while len(streams) == 0:
    streams = resolve_byprop("name", cfg.lsl_name, timeout=1)
    if len(streams) == 0:
        print(f"No eye-tracker streams found, retry ({tries})")
        tries += 1

print("eye-tracking stream found!!!")
inlet = StreamInlet(streams[0])

height = cfg.w_height // 2
width = cfg.w_width // 2
canvas = np.zeros((height, width), dtype=np.uint8)

buffer_len = 3
buffer_x = deque([], maxlen=buffer_len)
buffer_y = deque([], maxlen=buffer_len)

while True:
    canvas[:] = 0

    chunk, timestamps = inlet.pull_chunk()
    if timestamps:
        gaze_x = chunk[-1][4] / 2
        gaze_y = chunk[-1][5] / 2

        if not math.isnan(gaze_x) and not math.isnan(gaze_y):
            buffer_x.append(gaze_x)
            buffer_y.append(gaze_y)

            mean_x = int(np.nanmean(buffer_x))
            mean_y = int(np.nanmean(buffer_y))

            cv2.circle(canvas, (mean_x, mean_y), radius=20, color=255, thickness=-1)

    cv2.imshow("Real-Time Gaze Point", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty("Real-Time Gaze Point", cv2.WND_PROP_VISIBLE) < 1:
        break

    time.sleep(1 / 30)

cv2.destroyAllWindows()
