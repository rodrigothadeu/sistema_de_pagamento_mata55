import tkinter as tk
from tkinter import messagebox
from services.relatorio_pdf import gerar_relatorio_pdf

class RelatorioPDFView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Gerar Relatório PDF")
        self.window.geometry("300x150")

        tk.Label(self.window, text="Clique no botão abaixo para gerar o relatório", wraplength=280, justify="center").pack(pady=20)

        tk.Button(self.window, text="Gerar Relatório", command=self.gerar).pack(pady=10)

    def gerar(self):
        try:
            gerar_relatorio_pdf()
            messagebox.showinfo("Sucesso", "Relatório PDF gerado com sucesso!")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar o relatório.\n\n{str(e)}")
