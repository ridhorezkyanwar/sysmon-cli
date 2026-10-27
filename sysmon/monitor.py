"""System metric helpers used by the SysMon CLI."""

import os

import psutil


def get_cpu_usage() -> float:
    """Return the current CPU utilization percentage."""
    return psutil.cpu_percent(interval=1)


def get_memory_info() -> dict[str, float]:
    """Return total and used memory in GiB plus utilization percentage."""
    memory = psutil.virtual_memory()
    gib = 1024 ** 3
    return {
        "total": round(memory.total / gib, 2),
        "used": round(memory.used / gib, 2),
        "percent": float(memory.percent),
    }


def get_disk_info() -> dict[str, float]:
    """Return root-volume total/free space in GiB and utilization percentage."""
    root_path = os.path.abspath(os.sep)
    disk = psutil.disk_usage(root_path)
    gib = 1024 ** 3
    return {
        "total": round(disk.total / gib, 2),
        "free": round(disk.free / gib, 2),
        "percent": float(disk.percent),
    }
