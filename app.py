import tkinter as tk
from tkinter import ttk
from entry import EntryLogic


class IncomeTrackerApp:
    def __init__(self, window: tk.Tk):
        self.window = window

        self.window.geometry("900x540")
        self.window.title("Income & Expense Tracker")
        self.window.configure(bg="#f4f6f8")

        self.title_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.type_var = tk.StringVar(value="Income")
        self.description_var = tk.StringVar()
        self.amount_var = tk.IntVar()
        self.entries_logic = EntryLogic([])

        self._create_input_Area()
        self._create_table()
        self._create_summary_zone()

    def _create_input_Area(self):

        label_options = {"padx": 5, "pady": 5, "sticky": "w"}

        style = ttk.Style(self.window)
        style.configure("TLabel", background="#f4f6f8", foreground="#2f3b4f")
        style.configure("TButton", padding=6, font=("Segoe UI", 9))
        style.configure("Treeview", rowheight=24, fieldbackground="#ffffff")
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))

        tk.Label(self.window, text="Title", bg="#f4f6f8").grid(row=0, column=0, **label_options)
        tk.Entry(self.window, textvariable=self.title_var, border=2, relief="solid").grid(row=0, column=1, columnspan=2, padx=20, pady=5, sticky="ew")

        tk.Label(self.window, text="Date", bg="#f4f6f8").grid(row=1, column=0, **label_options)
        tk.Entry(self.window, textvariable=self.date_var, border=2, relief="solid").grid(row=1, column=1, columnspan=2, padx=20, pady=5, sticky="ew")

        tk.Label(self.window, text="Type", bg="#f4f6f8").grid(row=2, column=0, **label_options)
        tk.Radiobutton(self.window, text="Income", variable=self.type_var, value="Income", bg="#f4f6f8", activebackground="#f4f6f8").grid(row=2, padx=20, column=1, sticky="w")
        tk.Radiobutton(self.window, text="Expense", variable=self.type_var, value="Expense", bg="#f4f6f8", activebackground="#f4f6f8").grid(row=2, padx=20, column=2, sticky="w")

        tk.Label(self.window, text="Description", bg="#f4f6f8").grid(row=3, column=0, **label_options)
        tk.Entry(self.window, textvariable=self.description_var, width=15, border=2, relief="solid").grid(row=3, column=1, columnspan=2, padx=20, pady=5, sticky="ew")

        tk.Label(self.window, text="Amount", bg="#f4f6f8").grid(row=4, column=0, **label_options)
        tk.Entry(self.window, textvariable=self.amount_var, width=15, border=2, relief="solid").grid(row=4, column=1, columnspan=2, padx=20, pady=5, sticky="ew")



    
        # ------- Buttons ----------
        button_frame = tk.Frame(self.window, bg="#f4f6f8")
        button_frame.grid(row=5, column=0, columnspan=4, padx=20, pady=(10, 5), sticky="ew")

        button_frame.columnconfigure((0, 1, 2, 3), weight=1)

        add_button = tk.Button(button_frame, text="Add", command=self.add_entry, bg="#638ed8", fg="white", relief="groove")
        add_button.grid(row=0, column=0, padx=6, pady=0, sticky="ew")

        self.delete_button = tk.Button(button_frame, text="Delete", bg="#CFCFCF", fg="white", relief="ridge")
        self.delete_button.grid(row=0, column=1, padx=6, pady=0, sticky="ew")

        self.edit_button = tk.Button(button_frame, text="Edit", bg="#CFCFCF", fg="white", relief="ridge")
        self.edit_button.grid(row=0, column=2, padx=6, pady=0, sticky="ew")

        save_button = tk.Button(button_frame, text="Save", command=self.edit_entry, bg="#7EE45F", fg="white", relief="ridge")
        save_button.grid(row=0, column=3, padx=6, pady=0, sticky="ew")

        self.window.columnconfigure(1, weight=1)

    
    def _create_table(self):

        self.message_label = tk.Label(self.window, text="", bg="#f4f6f8", fg="#5b6470")
        self.message_label.grid(row=6, column=1, columnspan=2, padx=20, pady=(4, 8), sticky="w")

        columns = ("id", "title", "date", "description", "type", "amount")
        
        self.table = ttk.Treeview(self.window, columns=columns, show="headings")

        self.table.heading("id",text="ID")
        self.table.column("id", width=50, anchor=tk.CENTER)

        self.table.heading("title", text="Title")
        self.table.column("title",width=150, anchor=tk.W)

        self.table.heading("date",text="Date")
        self.table.column("date",width=120, anchor=tk.W)

        self.table.heading("description",text="Description")
        self.table.column("description",width=120, anchor=tk.W)

        self.table.heading("type", text="Type")
        self.table.column("type", width=70, anchor=tk.W)

        self.table.heading("amount",text="Amount")
        self.table.column("amount",width=120, anchor=tk.W)

        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=0)
        self.window.grid_rowconfigure(8, weight=1)

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        scrollbar.grid(row=8, column=2, sticky="ns", padx=(0, 0), pady=10)
        self.table.grid(row=8, column=1, columnspan=1, sticky="nsew", padx=(20, 0), pady=10)
        self.table.bind("<<TreeviewSelect>>", self._update_buttons)
        self._update_buttons()

        self.summary_label = tk.Label(self.window, text="Income: €0   Expense: €0   Net: €0", bg="#f4f6f8", fg="#2f3b4f")
        self.summary_label.grid(row=9, column=0, columnspan=2, padx=8, pady=(8, 4), sticky="w")

        

    def _create_summary_zone(self):
        self.summary_label = tk.Label(self.window, text="Income: €0   Expense: €0   Net: €0", bg="#f4f6f8", fg="#2f3b4f")
        self.summary_label.grid(row=9, column=0, columnspan=2, padx=8, pady=(8, 4), sticky="w")

    def _update_summary(self) -> None:
        income = self.entries_logic.get_income()
        expense = self.entries_logic.get_expenses()
        net = self.entries_logic.get_net_income()
        self.summary_label.config(text=f"Income: €{income}   Expense: €{expense}   Net: €{net}")

    def _update_buttons(self, event=None) -> None:
        if self.table.selection():
            self.delete_button.config(command=self.delete_entry, bg="#d86363", fg="white", relief="groove")
            self.edit_button.config(command=self.edit_entry, bg="#d6a439", fg="white", relief="groove")
        else:
            self.delete_button.config(command=None, bg="#CFCFCF", fg="white", relief="ridge")
            self.edit_button.config(command=None, bg="#CFCFCF", fg="white", relief="ridge")

    def _clear_form(self) -> None:
        self.title_var.set("")
        self.date_var.set("")
        self.type_var.set("Income")
        self.description_var.set("")
        self.amount_var.set(0)

    def add_entry(self) -> None:
        title = self.title_var.get().strip()
        date = self.date_var.get()
        entry_type = self.type_var.get().strip()
        description = self.description_var.get().strip()
        amount = self.amount_var.get()

        if not title or not description or not date or not entry_type or not amount:
            self.message_label.config(text="Fill all input fields before adding.")
            return

        if amount <= 0:
            self.message_label.config(text="Enter a positive amount.")
            return

        new_entry = self.entries_logic.add(title, date, entry_type, description, amount)
        self.table.insert(
            "",
            "end",
            iid=str(new_entry.id),
            values=(new_entry.id, new_entry.title, new_entry.date, new_entry.description, new_entry.type, new_entry.amount),
        )

        self._clear_form()
        self._update_summary()

    def delete_entry(self) -> None:
        try:
            selected_item = self.table.selection()
            values = self.table.item(selected_item[0])["values"]
            item_id = values[0]
            self.table.delete(selected_item)
            self.entries_logic.delete(item_id)
            self._update_summary()
            print("Successful deletion of: ", selected_item)
            
        except Exception as e:
            print(f"Unsucessful deletion of:", selected_item, "\n", e)
    
    
    def edit_entry():
        pass



if __name__ == "__main__":
    window = tk.Tk()
    IncomeTrackerApp(window)
    window.mainloop()