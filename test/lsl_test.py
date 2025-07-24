from helpers import LSLRecorder
from pylsl import StreamInlet, resolve_byprop
import os
import time


streams = resolve_byprop("name", "EyeLogic", timeout=1)
inlet = StreamInlet(streams[0])

save_dir = 'data/test/'
os.makedirs(save_dir, exist_ok=True)
recorder = LSLRecorder(inlet, os.path.join(save_dir, 'test_v10.csv'))
recorder.start()

for i in range(60):
    print(i)
    time.sleep(1)

recorder.end_run()
recorder.join()