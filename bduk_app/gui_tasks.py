import tkinter as tk
from tkinter import ttk, messagebox

import csv

DATA_FILE = 'bduk_app/bduk_tasks.csv'


def load_bduk_tasks():
    """Load task list for BDUK staff."""
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_full_dataset():
    """Retrieve full WORKBank dataset from Hugging Face if available."""
    try:
        from datasets import load_dataset
        ds = load_dataset(
            "SALT-NLP/WORKBank",
            data_files="task_data/task_statement_with_metadata.csv",
            split="train",
        )
        return ds
    except Exception as exc:
        messagebox.showerror("Dataset Error", f"Could not load dataset: {exc}")
        return None


class TaskBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BDUK Task Browser")
        self.geometry("700x400")
        self.tasks = load_bduk_tasks()
        self.dataset = None
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.task_list = tk.Listbox(frame)
        for task in self.tasks:
            self.task_list.insert(tk.END, task['task'])
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_list.bind("<<ListboxSelect>>", self.display_task_info)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.task_list.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.task_list.config(yscrollcommand=scrollbar.set)

        self.info_text = tk.Text(frame, wrap=tk.WORD)
        self.info_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        load_button = ttk.Button(self, text="Load Full Dataset", command=self.load_dataset)
        load_button.pack(pady=5)

    def display_task_info(self, event):
        sel = self.task_list.curselection()
        if not sel:
            return
        idx = sel[0]
        task = self.tasks[idx]
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"Task: {task['task']}\n\n")
        self.info_text.insert(tk.END, f"Research Finding:\n{task['research_finding']}")

    def load_dataset(self):
        if self.dataset is None:
            self.dataset = load_full_dataset()
            if self.dataset is None:
                return
        messagebox.showinfo("Dataset", f"Loaded {len(self.dataset)} tasks from WORKBank")


def main():
    app = TaskBrowser()
    app.mainloop()


if __name__ == '__main__':
    main()
