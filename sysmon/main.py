import argparse
from rich.console import Console
from rich.table import Table
from sysmon.monitor import get_cpu_usage, get_memory_info, get_disk_info

console = Console()

def display_metrics():
    table = Table(title="System Resource Monitor")
    table.add_column("Resource", justify="left", style="cyan", no_wrap=True)
    table.add_column("Usage / Value", style="magenta")

    # Ambil data
    cpu = get_cpu_usage()
    mem = get_memory_info()
    disk = get_disk_info()

    # Masukkan ke tabel
    table.add_row("CPU Usage", f"{cpu}%")
    table.add_row("Memory", f"{mem['used']}GB / {mem['total']}GB ({mem['percent']}%)")
    table.add_row("Disk (Root)", f"Free: {disk['free']}GB / {disk['total']}GB ({disk['percent']}% Used)")

    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="SysMon: A simple CLI system monitor.")
    parser.add_argument("--monitor", action="store_true", help="Display system metrics.")
    args = parser.parse_args()

    if args.monitor:
        display_metrics()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()