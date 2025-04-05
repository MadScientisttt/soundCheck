import sounddevice as sd
import numpy as np


#检测声音
def audio_callback(indata, frames, time, status):
    # indata包含音频数据，形状为(n_samples, n_channels)
    volume = np.linalg.norm(indata) * 10  # 计算音量

    if volume > THRESHOLD:  # 你的阈值
        print(f"检测到声音！音量级别: {volume}")


# 列出所有音频设备
print(sd.query_devices())

# 设置参数
device_id = 49  # 替换为你的采集卡设备ID
samplerate = 44100
blocksize = 1024
THRESHOLD = 5  # 需要根据实际情况调整

# 开始音频流
with sd.InputStream(device=device_id, channels=1, callback=audio_callback,
                    samplerate=samplerate, blocksize=blocksize):
    print("开始监听...按Ctrl+C停止")
    while True:
        sd.sleep(1000)