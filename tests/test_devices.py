from core.devices import DeviceManager
import pytest

def test_device_listing():
    mgr = DeviceManager()
    devices = mgr.get_devices()
    assert isinstance(devices, list)
    assert len(devices) > 0