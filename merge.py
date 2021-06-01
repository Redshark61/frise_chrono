import PyPDF2
import os
import os.path

# for pdf in os.listdir:
path = 'pdf/'
path_merged = 'merged pdf/'
onlyfiles = os.listdir(path)
i = 0
while i < len(onlyfiles):
    basename_without_ext = os.path.splitext(os.path.basename(onlyfiles[i]))[0]

    print(basename_without_ext)

    # Open the files that have to be merged one by one
    pdf1File = open('pdf/{}'.format(onlyfiles[i]), 'rb')
    pdf2File = open('pdf/{}'.format(onlyfiles[i+1]), 'rb')

    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('merged pdf/{}'.format(onlyfiles[i]), 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    i += 2
