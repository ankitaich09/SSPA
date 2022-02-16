import docx2txt

text = docx2txt.process("UCSD_IA_3011_Scene 1.docx")

with open("output_UCSD_IA_3011.txt", 'w') as tf:
    print(text, file=tf)
