import dropbox
import re
from dropbox.files import WriteMode

APPKEY = "5dloqjjbgv4lo45"
APPSECRET = "kvzfw40fkqhj9c0"
FOLDER_NAME = "ctn_images"
REFRESH_TOKEN = "mOBCN52hjrEAAAAAAAAAAT0EpmoawlynX2JV8D6ZCNi8D5sEBcQafm_RX_qxlO_N"
APP_TOKEN = "sl.BRflssQUvHnoAYZMmzSdLQscTgBF2L_vP4rr_QhF_CoJWBXW_VsIxk-P3Q5g3KovkvrYB4oYGDwwKLcQeJaGwMsDtNYxfHxM9QijIb45qznRRighvQQm2IF9Z9AbUA-AybRkw2UncnE"
# APP_TOKEN = "wQyrp3mhYbAAAAAAAAAAHF3wr7tM2rmC0gEWN5pXolk"
# Token Generated from dropbox


dbx = dropbox.Dropbox(app_key=APPKEY,
                      app_secret=APPSECRET,
                      oauth2_refresh_token=REFRESH_TOKEN)

existing_link = ''


class TransferData:

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        # print(f'the source {file_from}')
        # print(f' the dest {file_to}')

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

    def get_photo_link(self, filename):
        # re = dbx.files_get_thumbnail_v2(filename)
        st = str(dbx.files_get_temporary_link(filename))
        # print(re.search("(?P<url>https?://[^\s]+)", st).group("url"))
        return re.search("(?P<url>https?://[^']+)", st).group("url")

    def delete_file(self, file_path_to_delete):
        dbx.files_delete_v2(file_path_to_delete)

        return "file deleted successfully"

    def create_permanant_link(self, filename):
        global perm_link
        try:
            perm_link = dbx.sharing_create_shared_link_with_settings(filename).url
            print(f'created link is {perm_link}')
            perm_link = re.sub('=0$', '=1', perm_link)
            return perm_link

        except:
            print('Link already created')
            existing_link_metadata = dbx.sharing_list_shared_links(filename, cursor=None, direct_only=None)
            print(f'existing link...{existing_link_metadata}')
            for link in existing_link_metadata.links:
                perm_link = re.sub('=0$', '=1', link.url)
            return perm_link

    def get_permenant_link(self, filename):
        existing_link_metadata = dbx.sharing_list_shared_links(filename, cursor=None, direct_only=None)
        print(f'existing...{existing_link_metadata}')
