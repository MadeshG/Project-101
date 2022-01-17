import os
import dropbox

def upload(fileName):
    dropbox_access_token= "sl.A_-3Wjv16LC4G32SYSHzT-XV4NZ5EWxUr8kRfrgCoI9sxcaL8JKti3NKR1IS9Jd45ldaZ-njrC-N0BwPCDPvuhZ3HCUWCbOI2Gm2CFKnBILlr4it-nGFRa7J7LRrTrYQR36zNg0f8Kg"    
    dropbox_path= "/cloud/"+fileName
    computer_path="D:/Projects/Cloud storage/class 101/test.txt"
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")   
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))


files=os.listdir("D:/Projects/Cloud storage/class 101")
for file in files:
    print(file)
    upload(file)