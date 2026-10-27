from types import SimpleNamespace

from sysmon import monitor


def test_get_cpu_usage(monkeypatch):
    monkeypatch.setattr(monitor.psutil, "cpu_percent", lambda interval: 37.5)

    assert monitor.get_cpu_usage() == 37.5


def test_get_memory_info(monkeypatch):
    gib = 1024 ** 3
    monkeypatch.setattr(
        monitor.psutil,
        "virtual_memory",
        lambda: SimpleNamespace(total=8 * gib, used=3 * gib, percent=37.5),
    )

    assert monitor.get_memory_info() == {
        "total": 8.0,
        "used": 3.0,
        "percent": 37.5,
    }


def test_get_disk_info_uses_root_path_and_formats_values(monkeypatch):
    gib = 1024 ** 3
    calls = []
    monkeypatch.setattr(
        monitor.psutil,
        "disk_usage",
        lambda path: (
            calls.append(path)
            or SimpleNamespace(total=100 * gib, used=60 * gib, free=40 * gib, percent=60.0)
        ),
    )

    result = monitor.get_disk_info()

    assert calls == [monitor.os.path.abspath(monitor.os.sep)]
    assert result == {"total": 100.0, "free": 40.0, "percent": 60.0}
