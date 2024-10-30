import lusid_drive
import lusid_drive.models as models
import json
import logging
from lusid_drive.rest import ApiException


logger = logging.getLogger("drive-logger")
logger.setLevel("INFO")

def name_to_id(item_list, target_item):
    item_id = [obj.id for obj in item_list.values if obj.name == target_item]

    if len(item_id) != 1:
        # TODO: raise an exception due to no matching item name, or multiple matches
        pass

    else:
        return item_id[0]


# a path to id function would be useful to build here...


def get_folder_id(api_factory, folder_name):
    folders_api = api_factory.build(lusid_drive.api.FoldersApi)
    response = folders_api.get_root_folder(filter=f"name eq '{folder_name}'")
    folder_id = name_to_id(response, folder_name)

    return folder_id


def get_file_id(api_factory, file_name, folder_id):
    folders_api = api_factory.build(lusid_drive.api.FoldersApi)
    response = folders_api.get_folder_contents(folder_id, filter=f"name eq '{file_name}'")
    file_id = name_to_id(response, file_name)

    return file_id

def upload_file(
        files_api: lusid_drive.FilesApi,
        file_name: str,
        folder_path: str,
        body: str,
 ):
        
        try:
            x = files_api.create_file(
                x_lusid_drive_filename=file_name,
                x_lusid_drive_path=folder_path,
                content_length=len(body.encode('UTF-8')),
                body=body
                )
            logging.info(
                f"File created via the files API"
            )
            return x

        except lusid_drive.ApiException as e:
            detail = json.loads(e.body)
            if detail["code"] != 671:  # FileAlreadyExists
                raise e
            logging.exception(
                f"File already exists"
            )
            return detail

               
            

