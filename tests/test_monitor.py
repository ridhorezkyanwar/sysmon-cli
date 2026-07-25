from sysmon.monitor import get_cpu_usage, get_memory_info, get_disk_info

def test_get_cpu_usage():
    cpu = get_cpu_usage()
    assert isinstance(cpu, float)
    assert 0.0 <= cpu <= 100.0

def test_get_memory_info():
    mem = get_memory_info()
    assert "total" in mem
    assert "percent" in mem
    assert mem["percent"] >= 0.0

def test_get_disk_info():
    disk = get_disk_info()
    assert "free" in disk
    assert "percent" in disk
    assert disk["percent"] <= 100.0