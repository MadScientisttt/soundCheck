import sounddevice as sd
import numpy as np


# 列出监听设备
def list_input_devices():
    """列出所有输入设备并返回有效设备列表"""
    devices = sd.query_devices()
    input_devices = []
    print("\n可用的音频输入设备：")
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            status = "✅ 默认输入设备" if i == sd.default.device[0] else ""
            print(f"[{i}] {dev['name']} {status}")
            input_devices.append(i)
    return input_devices


# 选择监听设备
def select_device_interactive():
    # 交互式设备选择
    input_devices = list_input_devices()

    while True:
        try:
            choice = input("\n请输入设备编号（直接回车使用默认设备）: ").strip()
            if not choice:
                default_id = sd.default.device[0]
                print(f"使用默认输入设备 [ID: {default_id}]")
                return default_id

            device_id = int(choice)
            if device_id in input_devices:
                return device_id
            print(f"⚠️ 错误：设备 {device_id} 不是有效的输入设备，请重新选择")
        except ValueError:
            print("⚠️ 错误：请输入数字编号")


# 检测音量
def audio_callback(indata, frames, time, status):
    volume = np.linalg.norm(indata) * 10
    if volume > CONFIG["threshold"]:
        print(f"检测到声音！音量级别: {volume:.2f} dB")


# 程序配置
CONFIG = {
    "samplerate": 44100,
    "blocksize": 1024,
    "threshold": 0.5,
    "channels": 1
}

if __name__ == "__main__":
    try:
        # 交互式设备选择
        device_id = select_device_interactive()

        # 显示设备详细信息
        device_info = sd.query_devices(device_id)
        print("\n设备详细信息：")
        print(f"名称：{device_info['name']}")
        print(f"采样率范围：{device_info['default_samplerate']} Hz")
        print(f"输入声道数：{device_info['max_input_channels']}")

        # 开始监听
        with sd.InputStream(
                device=device_id,
                channels=CONFIG["channels"],
                samplerate=CONFIG["samplerate"],
                blocksize=CONFIG["blocksize"],
                callback=audio_callback
        ):
            print(f"\n开始监听 [设备ID: {device_id}]... 按 Ctrl+C 停止")
            while True:
                sd.sleep(1000)

    except KeyboardInterrupt:
        print("\n监听已停止")
    except Exception as e:
        print(f"发生错误: {str(e)}")
        print("建议检查：")
        print("1. 设备是否被其他程序占用")
        print("2. 是否选择了正确的输入设备")
        print("3. 系统音频设置是否正确")