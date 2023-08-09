import PyPDF2
import sys
import os

# Note :

#this program merges the fist pdf it finds with the second pdf
#that means that if pdf1 is before pdf2 , in the combined version
#pdf1 will come first that pdf2




#variable to store the file merger
merge = PyPDF2.PdfMerger()

#searches through all the files in the same directory
for file in os.listdir(os.curdir):
    
    #sorts out all the pdfs
    if file.endswith('.pdf'):
        
        #appends both the files
        merge.append(file)
        
    #combines both the pdfs and names it combinedPDF
    merge.write("combinedPDF.pdf")