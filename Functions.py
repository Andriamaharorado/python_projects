from docx2pdf import convert
import os

def convert_docs_to_pdfs(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.docx'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace('.docx', '.pdf'))
            convert(input_path, output_path)

# Spécifiez le répertoire d'entrée et de sortie
convert_docs_to_pdfs(input_directory, output_directory)
