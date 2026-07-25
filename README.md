# 💻 SysMon-CLI

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A lightweight, elegant command-line interface (CLI) tool to monitor system resources. Built entirely with Python, it extracts real-time CPU, Memory, and Disk metrics and presents them in a clean, human-readable terminal UI.

Designed with a focus on clean code, modularity, and testability, serving as a showcase for Python systems engineering and CLI packaging.

## ✨ Features

* **Core System Metrics:** Real-time tracking of CPU percentage, RAM allocation, and Root Disk usage using `psutil`.
* **Beautiful Terminal UI:** Styled and structured output using the `rich` library for maximum readability in the console.
* **Robust & Tested:** Covered by automated unit tests using `pytest` to ensure data accuracy and reliability.
* **Easily Packaged:** Configured with `pyproject.toml` for standard, seamless `pip` installation.

## 🚀 Installation

It is highly recommended to install this tool within a Python Virtual Environment (`venv`) to prevent dependency conflicts with your system packages.

```bash
# 1. Clone the repository
git clone [https://github.com/ridhorezkyanwar/sysmon-cli.git](https://github.com/ridhorezkyanwar/sysmon-cli.git)
cd sysmon-cli

# 2. Create and activate a virtual environment
python -m venv venv

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate

# 3. Install the package and dependencies
pip install -e .

🛠️ Usage
Once installed, the CLI tool is registered to your path. You can run it directly from your terminal:

Bash
sysmon --monitor
Example Output:

Plaintext
                 System Resource Monitor                
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Resource    ┃ Usage / Value                       ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ CPU Usage   │ 15.1%                               │
│ Memory      │ 10.66GB / 15.68GB (68.0%)           │
│ Disk (Root) │ Free: 46.5GB / 72.46GB (35.8% Used) │
└─────────────┴─────────────────────────────────────┘
🧪 Running Tests
To verify that the core logic and metric calculations are functioning correctly, run the included test suite:

Bash
pytest tests/


👨‍💻 Author
Ridho Rezky Anwar
Self-taught Python & Systems Developer