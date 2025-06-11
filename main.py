'''
PDF handling using Python

Operations performed
    - Create pdf
    - Merge n number of pdf
    - Set Password
    - Revoke Password
'''
import img2pdf
from pypdf import PdfReader, PdfWriter

def create_pdf():
    images = []
    try:
        n = int(input("Enter total no of images (with extension) : "))
        for i in range(1,n+1):
            try:
                name = input(f"Enter name of {i} images : ")
                images.append(name)
            except Exception as e:
                print(e)
        pdf = img2pdf.convert(images)

        with open("merged-pdf.pdf", "wb") as f:
            f.write(pdf)
    except:
        print("Error occured")

def merge_pdfs():
    merger = PdfWriter()
    try:
        n = int(input("Enter total pdf you wanna merge : "))
        pdfs = []
        for i in range (0,n):
            name = input(f"Enter name of {i+1} pdf : ")
            pdfs.append(name)

        for pdf in pdfs:
            merger.append(pdf)

        merger.write("merged-multiple.pdf")
        merger.close()
    except FileNotFoundError:
        print("File not found")

def encrypt_pdf():
    pdf = input("Enter name of pdf which should be ecrypted : ")

    reader = PdfReader(pdf)
    writer = PdfWriter(clone_from=reader)

    if reader.is_encrypted:
        print("Pdf already encrypted")
    else:
        password = input("Enter password : ")
        writer.encrypt(password)
        with open(f"encrypted {pdf}", "wb") as f:
            writer.write(f)
        print("Password Set Successfully")

def decrypt_pdf():
    pdf = input("Enter pdf name which should be decrypted : ")
    reader = PdfReader(pdf)

    if reader.is_encrypted:
        password = input("Enter current password to decrypt : ")
        reader.decrypt(password)
        writer = PdfWriter(clone_from=reader)
        with open(f"decrypted {pdf}", "wb") as f:
            writer.write(f)
        print("Operation Done")
    else:
        print("Already decrypted")


print("This is PDF handler")
print("!********Operations Possible************!")
print("1. Create pdf")
print("2. Merge pdfs")
print("3. Encrypt pdf")
print("4. Decrypt pdf")
while True:
    i = int(input("Enter choice(1/2/3/4) : "))
    if i not in [1,2,3,4]:
        print("Please enter valid choice!")
        continue
    break
match(i):
    case 1:create_pdf()
    case 2:merge_pdfs()
    case 3:encrypt_pdf()
    case 4:decrypt_pdf()
