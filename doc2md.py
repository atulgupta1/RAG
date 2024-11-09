import docx2txt

def convert_docx_to_md(docx_file, md_file):
  """Converts a given .docx file to a .md file.

  Args:
    docx_file: Path to the input .docx file.
    md_file: Path to the output .md file.
  """

  text = docx2txt.process(docx_file)
  with open(md_file, 'w', encoding='utf-8') as f:
    f.write(text)

# Example usage:
docx_file = "21101-840.docx"
md_file = "output.md"
convert_docx_to_md(docx_file, md_file)