import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, time, status="Belum Selesai"):
        self.name = name
        self.time = time
        self.status = status

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def __str__(self):
        return f"{self.name} - {self.time} - {self.status}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="#f7f7f7")
        self.tasks = []  

        # Tampilan awal
        self.create_start_screen()

    def create_start_screen(self):

        self.start_screen = tk.Frame(self.root, bg="#f7f7f7")
        self.start_screen.pack(fill="both", expand=True)

        welcome_label = tk.Label(self.start_screen,
            text="🌟 Welcome to To-Do List 🌟",bg="#f7f7f7",fg="#AC6759",font=("Arial", 24, "bold"),)
        welcome_label.pack(pady=100)

        start_button = tk.Button(self.start_screen,
            text="Mulai",command=self.start_app,bg="#9D9383",fg="white",font=("Arial", 16, "bold"),width=15,)
        start_button.pack(pady=20)

    def start_app(self):
        
        self.start_screen.destroy()
        self.create_main_screen()

    def create_main_screen(self):
        # Membuat tampilan utama aplikasi.
        header = tk.Label(self.root, text="To-Do List", bg="#AC6759", fg="white", font=("Arial", 24, "bold"))
        header.pack(fill="x")

        # input tugas
        input_frame = tk.Frame(self.root, bg="#f7f7f7")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
        self.task_entry.grid(row=0, column=0, padx=5)

        hours = [f"{h:02d}" for h in range(24)]
        self.hour_var = tk.StringVar(value="00")
        hour_menu = tk.OptionMenu(input_frame, self.hour_var, *hours)
        hour_menu.config(font=("Arial", 12), bg="#E5DAC6", width=5)
        hour_menu.grid(row=0, column=1, padx=5)

        minutes = [f"{m:02d}" for m in range(60)]
        self.minute_var = tk.StringVar(value="00")
        minute_menu = tk.OptionMenu(input_frame, self.minute_var, *minutes)
        minute_menu.config(font=("Arial", 12), bg="#E5DAC6", width=5)
        minute_menu.grid(row=0, column=2, padx=5)

        add_button = tk.Button(input_frame, text="Tambah", command=self.add_task, bg="sienna", fg="white", font=("Arial", 12, "bold"))
        add_button.grid(row=0, column=3, padx=5)

        # List tugas
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bg="#e8e8e8", selectbackground="#4CAF50")
        self.task_listbox.pack(pady=10)

        # Tombol lain
        action_frame = tk.Frame(self.root, bg="#f7f7f7")
        action_frame.pack()

        done_button = tk.Button(action_frame, text="Selesai", command=self.mark_done, bg="#E08F71", fg="white", font=("Arial", 12, "bold"))
        done_button.grid(row=0, column=0, padx=5)

        delete_button = tk.Button(action_frame, text="Hapus", command=self.delete_task, bg="#F1C7B9", fg="white", font=("Arial", 12, "bold"))
        delete_button.grid(row=0, column=1, padx=5)

        archive_button = tk.Button(action_frame, text="Arsip", command=self.view_archive, bg="#FEC195", fg="white", font=("Arial", 12, "bold"))
        archive_button.grid(row=0, column=2, padx=5)

        # Arsip 
        self.archive = []

    def add_task(self):
        # Menambahkan tugas 
        task_name = self.task_entry.get()
        task_time = f"{self.hour_var.get()}:{self.minute_var.get()}"

        if task_name:
            new_task = Task(task_name, task_time)
            self.tasks.append(new_task)  
            self.tasks.sort(key=lambda t: t.time)  
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Tidak Valid", "Masukkan nama tugas!")

    def mark_done(self):
     
        while True:
            selected_items = self.task_listbox.curselection()
            if selected_items:
                selected_index = selected_items[0]
                selected_task = self.tasks[selected_index]
                selected_task.set_status("Selesai")
                self.archive.append(selected_task)  # Pindah ke arsip
                del self.tasks[selected_index]  
                self.update_task_list()
                break 
            else:
                messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")
                break  

    def delete_task(self):
        while True:
            selected_items = self.task_listbox.curselection()
            if selected_items:
                selected_index = selected_items[0]
                del self.tasks[selected_index]
                self.update_task_list()
                break  
            else:
                messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!") 
                break  

    def view_archive(self):
        archive_window = tk.Toplevel(self.root)
        archive_window.title("Arsip Tugas")
        archive_window.configure(bg="#f7f7f7")

        archive_listbox = tk.Listbox(archive_window, width=50, height=10, font=("Arial", 12), bg="#e8e8e8")
        archive_listbox.pack(pady=10)

        for task in self.archive:
            archive_listbox.insert(tk.END, str(task))

        close_button = tk.Button(archive_window, text="Tutup", command=archive_window.destroy, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
        close_button.pack(pady=10)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
