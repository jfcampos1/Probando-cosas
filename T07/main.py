__author__ = 'JuanFrancisco'
import sys

from PyQt4 import QtGui
from dropbox import DropboxOAuth2FlowNoRedirect
from dropbox import Dropbox

from Gui import MainForm

APP_KEY = 'cbm74gzdx3jn00g'
APP_SECRET = 'chq2mprrc8ldtfg'
auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    access_token, user_id = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))

client = Dropbox(access_token)
app = QtGui.QApplication([])
ventana = MainForm(client)
ventana.show()
sys.exit(app.exec_())
