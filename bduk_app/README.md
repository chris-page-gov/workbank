# BDUK Task Browser

This directory contains small applications to help Building Digital UK (BDUK) staff browse candidate tasks and view associated research findings.

## Command Line Browser

Run the script using Python:

```bash
python bduk_app/browse_tasks.py
```

The application will display a numbered list of tasks. Enter the corresponding number to see the related research finding. Enter `0` to exit.

## Graphical Browser

A simple Tkinter-based GUI is available in `gui_tasks.py`. It loads the same BDUK task file and optionally retrieves the full WORKBank dataset from Hugging Face using the `datasets` library.

Run the GUI with:

```bash
python bduk_app/gui_tasks.py
```

Use the *Load Full Dataset* button to attempt downloading the full dataset as described in the repository README. If the environment lacks internet access or the `datasets` package, an error message will be shown.
