import sounddevice as sd


def list_input_devices():
    """列出所有输入设备"""
    devices = sd.query_devices()
    input_devices = []
    print("\n可用的音频输入设备：")
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            status = "✅ 默认输入设备" if i == sd.default.device[0] else ""
            print(f"[{i}] {dev['name']} {status}")
            input_devices.append(i)
    return input_devices


def select_device_interactive():
    """交互式设备选择"""
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
            print(f"错误：设备 {device_id} 无效")
        except ValueError:
            print("请输入数字编号")