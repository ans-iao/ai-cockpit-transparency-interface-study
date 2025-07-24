import pandas as pd
import numpy as np

data_path = "data/test/test_v10.csv"
df = pd.read_csv(data_path, sep=";")

test_time = 60

total_time = (df['Timestamp'].iloc[-1] - df["Timestamp"].iloc[0]) / 60

frame_numbers = df['FrameNumber'].to_numpy()
diffs = np.diff(frame_numbers)
frame_loss_arg = np.argwhere(diffs > 1).squeeze()
frame_loss = diffs[frame_loss_arg].sum()

print(f"Total samples: {df.shape[0]}/{test_time*250} ({df.shape[0]/(test_time*250) * 100:.3f} %)")
print(f"Total Time (Diff first/last sample): {total_time:.3f} min")
print(f"Average time diff between samples: {df['Timestamp'].diff().mean()}")
print(f"Frame loss: {frame_loss}/{df.size} ({frame_loss/df.size * 100:.3f} %)")
