import os
from pypdf import PdfWriter

def merge_pdfs(folder_path):
	# Initialize PdfWriter object
	writer = PdfWriter()

	# Get a sorted list of all PDF files in the folder
	pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])

	# If no pdf files found, abort.
	if len(pdf_files) == 0:
		print("No pdf files found. Aborting.")
		return

	# Loop through the sorted list and append each PDF to the merger
	for pdf in pdf_files:
		pdf_path = os.path.join(folder_path, pdf)
		writer.append(pdf_path)
		print(f"Added {pdf_path}")

	output_path = os.path.join(folder_path, 'Output')
	os.makedirs(output_path, exist_ok=True)
	
	# Write out the merged PDF to the specified output path
	writer.write(os.path.join(output_path, 'MergePdfOutput.pdf'))
	writer.close()
	
	print(f"All PDFs merged into {output_path}")


def script():
	folder = os.getcwd()
	
	proceed = input(f"Will merge all pdfs found in folder: {folder}\nProceed? (y/n):")
	if proceed.lower() == "y":
		merge_pdfs(folder)
