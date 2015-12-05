import dropbox
import os
import sys
import webbrowser
import dropbox
from PyQt4 import QtGui
import sys
from Gui import MainForm

client = dropbox.Dropbox('oZIp7HD8K0MAAAAAAAAAmmL1RtALYhBpWvXWvnHMkB62Zxgig0etOSEOgaVNEinV')
print('linked account: ', client.sharing_list_folders())
print(client.users_get_current_account())
hey = client.users_get_current_account()
print(hey.name.display_name)
# client.files_list_folder(path='/path/in/Dropbox')
for entry in client.files_list_folder('').entries:
    print(entry)
print(len(client.files_list_folder('').entries))
for i in client.files_list_folder('',recursive=True).entries:
    print(i)
print(len(client.files_list_folder('',recursive=True).entries))
#
# class ConfigObj:
#     def __init__(self,path):
#         self.key = 'juanfra_campos2@hotmail.com'
#         self.secret = '1comoestas'
#         self.path=path
########################################################################
#
#
# class DropObj(object):
#     """
#     Dropbox object that can access your dropbox folder,
#     as well as download and upload files to dropbox
#     """
#
#     #----------------------------------------------------------------------
#     def __init__(self, filename=None, path='/'):
#         """Constructor"""
#         self.base_path = os.path.dirname(os.path.abspath(__file__))
#         self.filename = filename
#         self.path = path
#         self.client = None
#
#         config_path = os.path.join(self.base_path, "config.ini")
#         # if os.path.exists(config_path):
#         #     try:
#         #         cfg = ConfigObj(config_path)
#         #     except IOError:
#         #         print ("ERROR opening config file!")
#         #         sys.exit(1)
#         #     self.cfg_dict = cfg.dict()
#         # else:
#         #     print ("ERROR: config.ini not found! Exiting!")
#         #     sys.exit(1)
#
#         self.connect()
#         self.list_folder()
#     #----------------------------------------------------------------------
#     def connect(self):
#         """
#         Connect and authenticate with dropbox
#         """
#         # app_key = self.cfg_dict["key"]
#         # app_secret = self.cfg_dict["secret"]
#         #
#         # access_type = "dropbox"
#         # session = dropbox.session.DropboxSession(app_key,
#         #                                          app_secret,
#         #                                          access_type)
#         #
#         # request_token = session.obtain_request_token()
#         #
#         # url = session.build_authorize_url(request_token)
#         # msg = "Opening %s. Please make sure this application is allowed before continuing."
#         # print( msg % url)
#         # webbrowser.open(url)
#         # input("Press enter to continue")
#         # access_token = session.obtain_access_token(request_token)
#
#         self.client = dropbox.Dropbox('oZIp7HD8K0MAAAAAAAAAmmL1RtALYhBpWvXWvnHMkB62Zxgig0etOSEOgaVNEinV')
#
#     #----------------------------------------------------------------------
#     def download_file(self, filename=None, outDir=None):
#         """
#         Download either the file passed to the class or the file passed
#         to the method
#         """
#
#         if filename:
#             fname = filename
#             f, metadata = self.client.get_file_and_metadata("/" + fname)
#         else:
#             fname = self.filename
#             f, metadata = self.client.get_file_and_metadata("/" + fname)
#
#         if outDir:
#             dst = os.path.join(outDir, fname)
#         else:
#             dst = fname
#
#         with open(fname, "w") as fh:
#             fh.write(f.read())
#
#         return dst, metadata
#
#     #----------------------------------------------------------------------
#     def get_account_info(self):
#         """
#         Returns the account information, such as user's display name,
#         quota, email address, etc
#         """
#         return self.client.account_info()
#
#     #----------------------------------------------------------------------
#     def list_folder(self, folder=None):
#         """
#         Return a dictionary of information about a folder
#         """
#         if folder:
#             folder_metadata = self.client.metadata(folder)
#         else:
#             folder_metadata = dropbox.files.Metadata("/")
#         return folder_metadata
#
#     #----------------------------------------------------------------------
#     def upload_file(self):
#         """
#         Upload a file to dropbox, returns file info dict
#         """
#         try:
#             with open(self.filename) as fh:
#                 path = os.path.join(self.path, self.filename)
#                 res = self.client.put_file(path, fh)
#                 print ("uploaded: ", res)
#         except Exception:
#             print ("ERROR: ", Exception)
#
#         return res
#
# if __name__ == "__main__":
#     drop = DropObj("somefile.txt")