# gnome-boxes-rpc

A lightweight Python script that launches **Gnome Boxes** and displays a custom, humorous Discord Rich Presence (RPC) status. It cycles through various "dummy" activities while tracking the total elapsed time since the application started.

## Features

* **Auto-Launch:** Starts `gnome-boxes` automatically via subprocess.
* **Dynamic Status:** Cycles through random "IT nightmare" phrases (e.g., "Deleting system32", "Trapped inside Vim").
* **Variable Duration:** Each phrase lasts for a specific, pre-defined amount of time.
* **Continuous Timer:** The Discord timer counts the total uptime of the session, not just the duration of the current phrase.
* **Smart Exit:** Automatically detects when the Gnome Boxes window is closed and kills the RPC connection immediately.

## Prerequisites

* Python 3
* Gnome Boxes (`sudo apt install gnome-boxes` or equivalent)
* `pypresence` library

## Installation

1.  **Install the dependency:**
    ```bash
    pip install pypresence
    ```

2.  **Save the script:**
    Save the Python code as `gnome-boxes-rpc.py`.

3.  **Make it executable:**
    ```bash
    chmod +x gnome-boxes-rpc.py
    ```

## Usage

Run the script from your terminal:

```bash
./gnome-boxes-rpc.py
