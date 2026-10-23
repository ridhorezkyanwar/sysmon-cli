# SysMon-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python badge" />
  <img src="https://img.shields.io/badge/CLI-555555?style=flat-square&logo=gnubash&logoColor=white" alt="CLI badge" />
  <img src="https://img.shields.io/badge/psutil-3572A5?style=flat-square" alt="psutil badge" />
</p>

A Python command-line utility that displays a snapshot of CPU usage, memory utilization, and root-disk usage in a readable terminal table.

## Features

- Reports CPU utilization.
- Displays used and total memory, plus utilization percentage.
- Displays free and total space for the root disk.
- Uses `psutil` to collect system metrics and `rich` to format terminal output.
- Includes tests for the system-metric helper functions.

## Requirements

- Python
- `pip`

## Install from source

```bash
git clone https://github.com/ridhorezkyanwar/sysmon-cli.git
cd sysmon-cli
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install the project and its runtime dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage

Display the current metrics:

```bash
sysmon --monitor
```

The command displays a single snapshot each time it runs; it is not a continuous polling monitor.

## Run tests

Install pytest in the active environment if it is not already available, then run:

```bash
python -m pip install pytest
python -m pytest tests/
```

## Project layout

```text
sysmon/
  main.py       # CLI arguments and terminal output
  monitor.py    # CPU, memory, and disk metric helpers
tests/
  test_monitor.py
pyproject.toml  # Package metadata and sysmon entry point
```

## Author

Ridho Rezky Anwar
