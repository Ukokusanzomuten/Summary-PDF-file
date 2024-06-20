import fitz  # PyMuPDF

# PDFを読み込む関数
def read_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "pdf\\sample.pdf"
    result = read_pdf(pdf_path)
    print(result)