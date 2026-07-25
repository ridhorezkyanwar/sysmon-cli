import psutil
def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_info() -> dict:
    mem = psutil.virtual_memory()
    return {
        "total": round(mem.total / (1024 ** 3), 2),
        "used": round(mem.used / (1024 ** 3), 2),
        "percent": mem.percent
    }
    
def get_disk_info() -> dict:
    disk = psutil.disk_usage('/')
    return {
        "total": round(disk.total / (1024 ** 3), 2),
        "free": round(disk.free / (1024 ** 3), 2),
        "percent": disk.percent
    }