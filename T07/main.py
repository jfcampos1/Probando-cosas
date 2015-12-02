__author__ = 'JuanFrancisco'
import dropbox
from PyQt4 import QtGui

from Gui import MainForm

client = dropbox.Dropbox('oZIp7HD8K0MAAAAAAAAAmmL1RtALYhBpWvXWvnHMkB62Zxgig0etOSEOgaVNEinV')
print('linked account: ', client.sharing_list_folders())
print(client.users_get_current_account())
hey = client.users_get_current_account()
print(hey.name.display_name)
# client.files_list_folder(path='/path/in/Dropbox')
for entry in client.files_list_folder('').entries:
    print(entry)
    # if type(entry)==FolderMetadata:
    #     for i in client.files_list_folder(entry.path_lower).entries:
    #         print(i)
# path='C:\\Users\\JuanFrancisco\\Downloads\\dropbox-planes.jpg'
# with open("{}".format(path), 'rb') as file:
#             archivo = file.read()
# print(client.files_list_folder('').entries)
# client.files_upload(archivo,path='/dropbox-planes.jpg',mute=True)
app = QtGui.QApplication([])
ventana = MainForm(client)
ventana.show()
app.exec_()

# f = open('working-draft.txt', 'rb')
# response = client.put_file('/magnum-opus.txt', f)
# print ('uploaded: ', response)
#
# folder_metadata = client.metadata('/')
# print ('metadata: ', folder_metadata)
#
# f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
# out = open('magnum-opus.txt', 'wb')
# out.write(f.read())
# out.close()
# print(metadata)
