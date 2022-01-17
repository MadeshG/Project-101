import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.realpath(local_path,file_from)
                dropBox_path = os.path.join(file_to,relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropBox_path,mode=WriteMode('over_write'))

def main():
    access_token = 'sl.A_5ZQzqjSC_3EzVsF5vFICff-CwzpXLc-U2E_LtMJfN6F2Oitg-L77joX47jkzx0IlaI4riAyYI0-hyCHGwzEtqw2eWZ0ZNR0MTwl5tcX7MmQlXJnbumIszMfrlBEM-tqKVnBOH5bUE'
    transferData = TransferData(access_token)

    file_from = str(input("enter the folder path to transfer"))
    file_to =   input("enter the full path to upload to dropbox")
    
    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()