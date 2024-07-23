import tkinter as tk
from tkinter import filedialog, messagebox
from file_manager import FileManager

class FileManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")

        self.zip_file_label = tk.Label(root, text="ZIP файл:")
        self.zip_file_label.pack()
        self.zip_file_entry = tk.Entry(root, width=50)
        self.zip_file_entry.pack()
        self.zip_file_button = tk.Button(root, text="Обзор", command=self.browse_zip_file)
        self.zip_file_button.pack()

        self.dest_dir_label = tk.Label(root, text="Директория назначения:")
        self.dest_dir_label.pack()
        self.dest_dir_entry = tk.Entry(root, width=50)
        self.dest_dir_entry.pack()
        self.dest_dir_button = tk.Button(root, text="Обзор", command=self.browse_dest_dir)
        self.dest_dir_button.pack()

        self.extensions_label = tk.Label(root, text="Названия папок для расширений (например, .txt:Тексты; .jpg:Изображения):")
        self.extensions_label.pack()
        self.extensions_entry = tk.Entry(root, width=50)
        self.extensions_entry.pack()

        self.organize_button = tk.Button(root, text="Организовать файлы", command=self.organize_files)
        self.organize_button.pack()

    def browse_zip_file(self):
        filename = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
        if filename:
            self.zip_file_entry.delete(0, tk.END)
            self.zip_file_entry.insert(0, filename)

    def browse_dest_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dest_dir_entry.delete(0, tk.END)
            self.dest_dir_entry.insert(0, directory)

    def organize_files(self):
        source_zip = self.zip_file_entry.get()
        destination_dir = self.dest_dir_entry.get()
        extensions = self.extensions_entry.get()
        folder_names = {ext.strip(): name.strip() for ext, name in (pair.split(":") for pair in extensions.split(";"))}

        if not source_zip or not destination_dir or not extensions:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
            return

        try:
            file_manager = FileManager(source_zip, destination_dir, folder_names)
            file_manager.extract_and_organize_files()
            messagebox.showinfo("Успех", "Файлы успешно организованы.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))




def main():
    root = tk.Tk()
    app = FileManagerUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()