# coding: utf-8

import os
from azure.storage.blob import BlockBlobService, PublicAccess

def send_image():
    try:
        # ストレージアカウントのkeyを入力
        account_name = 'handson20180423'  # ご自身のストレージアカウント名
        account_key  = 'OOhkhHGJ88hZyAPDp5++mohna3lZhSoV8e3/9DtebcvCkNxfc1q7pdgw7ICD01ClgSLVjpiV4qe+UCk1WBMvkw=='  # 取得したキー

        # Blobのアカウントに接続
        block_blob_service = BlockBlobService(account_name=account_name, account_key=account_key)

        # コンテナに接続
        container_name ='img'
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # アップロードするファイルを設定
        localpath = os.path.expanduser("~/Desktop")
        filename  = 'profile_yoshizaki.jpg'
        filepath  =os.path.join(localpath, filename)

        # 指定したBlobにfilenameでfilepathのファイルをアップロード
        print("Uploading to Blob storage as blob: " + filename)
        block_blob_service.create_blob_from_path(container_name, filename, filepath)

    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    send_image()
