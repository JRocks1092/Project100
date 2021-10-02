import dropbox
import os


def upload_file(file, uploadpath):
    access_token = "sl.A5m4fKq56SGjFs77hGnmCa0r_EPcMlgMr2WUOHXBAk61kepTY2UBQ2alnk2HScpVDJba2HL6y3TLxuD1OnFLiy5s7AVmnpPNSIjCe-hbK6Q3YGITv_2IpjQ8VJBwSrLIu1yARRrz2oE"
    file_from = file
    file_to = "/upload Files/"+uploadpath    
    print(file_to)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


path = input("Enter Path : ")
path = path.replace("/", "\\")

if os.path.exists(path):
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            filePath = os.path.join(root, name)
            fileRelPath = os.path.relpath(filePath, path)            
            upload_file(filePath, name)
else:
    print("No Folder with such name....")
