# 默认配置参数
DEFAULT_CONFIG = {
    "samplerate": 44100,
    "blocksize": 1024,
    "threshold": 0.5,
    "channels": 1
}

def load_config(config_path: str = None) -> dict:
    """加载配置文件（可扩展为从文件读取）"""
    # 此处可添加JSON/YAML文件加载逻辑
    return DEFAULT_CONFIG.copy()