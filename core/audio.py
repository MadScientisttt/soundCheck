import numpy as np
import sounddevice as sd


class AudioMonitor:
    def __init__(self, config: dict):
        self.config = config
        self.stream = None

    def audio_callback(self, indata, frames, time, status):
        """音频数据回调处理"""
        volume = np.linalg.norm(indata) * 10
        if volume > self.config["threshold"]:
            print(f"检测到声音！音量级别: {volume:.2f} dB")

    def start_monitoring(self, device_id: int):
        """启动监听"""
        self.stream = sd.InputStream(
            device=device_id,
            channels=self.config["channels"],
            samplerate=self.config["samplerate"],
            blocksize=self.config["blocksize"],
            callback=self.audio_callback
        )
        self.stream.start()

    def stop_monitoring(self):
        """停止监听"""
        if self.stream:
            self.stream.stop()
            self.stream.close()