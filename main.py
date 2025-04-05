from config.settings import load_config
from core.devices import select_device_interactive
from core.audio import AudioMonitor
import sounddevice as sd


def main():
    # 初始化配置
    config = load_config()

    try:
        # 设备选择
        device_id = select_device_interactive()

        # 显示设备信息
        device_info = sd.query_devices(device_id)
        print("\n设备详细信息：")
        print(f"名称：{device_info['name']}")
        print(f"采样率：{device_info['default_samplerate']} Hz")
        print(f"输入声道：{device_info['max_input_channels']}")

        # 启动监听
        monitor = AudioMonitor(config)
        monitor.start_monitoring(device_id)
        print(f"\n开始监听 [设备ID: {device_id}]... 按 Ctrl+C 停止")

        # 保持主线程运行
        while True:
            sd.sleep(1000)

    except KeyboardInterrupt:
        print("\n监听已停止")
    except Exception as e:
        print(f"发生错误: {str(e)}")
    finally:
        if 'monitor' in locals():
            monitor.stop_monitoring()


if __name__ == "__main__":
    main()