import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
import os

def merge_pdfs():
    # Ask the user to select multiple PDF files
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if not pdf_files:
        return

    # Ask the user to select a location to save the merged PDF
    save_path = filedialog.asksaveasfile(
        title="Save Merged PDF As",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if not save_path:
        return

    save_path = save_path.name if save_path else None

    if not save_path.endswith('.pdf'):
        save_path += '.pdf'

    # Merge the selected PDF files
    pdf_merger = PdfMerger()
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # Write the merged PDF to the selected location
    with open(save_path, "wb") as output_pdf:
        pdf_merger.write(output_pdf)

    pdf_merger.close()
    
    result_label.config(text=f"Merged PDF saved to:\n{save_path}")

# Create the main window
root = tk.Tk()
root.title("PDF Merger")

# Create and configure the "Merge PDFs" button
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()
