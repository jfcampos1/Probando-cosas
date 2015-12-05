__author__ = 'JuanFrancisco'
from dropbox import DropboxOAuth2Flow

# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
from dropbox import DropboxOAuth2Flow

# def get_dropbox_auth_flow(web_app_session):
#     redirect_uri = "https://my-web-server.org/dropbox-auth-finish"
#     return DropboxOAuth2Flow(
#         APP_KEY, APP_SECRET, redirect_uri, web_app_session,
#         "dropbox-auth-csrf-token")
#
# # URL handler for /dropbox-auth-start
# def dropbox_auth_start(web_app_session, request):
#     authorize_url = get_dropbox_auth_flow(web_app_session).start()
#     redirect_to(authorize_url)
#
# # URL handler for /dropbox-auth-finish
# def dropbox_auth_finish(web_app_session, request):
#     try:
#         access_token, user_id, url_state = \
#                 get_dropbox_auth_flow(web_app_session).finish(
#                     request.query_params)
#     except BadRequestException as e:
#         http_status(400)
#     except BadStateException as e:
#         # Start the auth flow again.
#         redirect_to("/dropbox-auth-start")
#     except CsrfException as e:
#         http_status(403)
#     except NotApprovedException as e:
#         flash('Not approved?  Why not?')
#         return redirect_to("/home")
#     except ProviderException as e:
#         logger.log("Auth error: %s" % (e,))
#         http_status(403)

from dropbox import DropboxOAuth2FlowNoRedirect
from dropbox import Dropbox

APP_KEY='cbm74gzdx3jn00g'
APP_SECRET='chq2mprrc8ldtfg'
auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print ("1. Go to: " + authorize_url)
print ("2. Click \"Allow\" (you might have to log in first).")
print ("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    access_token, user_id = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))

dbx = Dropbox(access_token)
print(dbx.users_get_current_account())