import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    # Tkinterウィンドウを作成し、隠す
    root = tk.Tk()
    root.withdraw()
    
    # ファイルダイアログを開き、PDFファイルを選択
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="PDFファイルを開いてください"
    )
    
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected")
    return file_path

if __name__ == "__main__":
    select_pdf_file()