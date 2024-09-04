import src.inputs as inputs
import time
from selenium.webdriver.common.by import By
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
import json
import os
import io


def month_to_int(month):
    if month == 'sausio':
        month = 1
    elif month == 'vasario':
        month = 2
    elif month == 'kovo':
        month = 3
    elif month == 'balandžio':
        month = 4
    elif month == 'gegužio':
        month = 5
    elif month == 'birželio':
        month = 6
    elif month == 'liepos':
        month = 7
    elif month == 'rugpjūčio':
        month = 8
    elif month == 'rugsėjo':
        month = 9
    elif month == 'spalio':
        month = 10
    elif month == 'lapkričio':
        month = 11
    elif month == 'gruodžio':
        month = 12
    return month


def creator(config):
    # Create a dictionary to represent the JSON data
    data = {'glass': [], 'paper': [], 'mixed': []}
    # Write the dictionary to a JSON file
    with open('data/' + config.street_name + config.house_name + '.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)  # 'indent=4' makes the JSON pretty-printed


def writer(config, trash, date):
    # Read the existing JSON file
    with open('data/' + config.street_name + config.house_name + '.json', 'r') as json_file:
        data = json.load(json_file)

    data[trash].append(date)  # Adding a new date
    with open('data/' + config.street_name + config.house_name + '.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


def reader(file):
    # # Read the existing JSON file
    # with open(file, 'r') as json_file:
    #     data = json.load(json_file)
    #
    # print(data)


    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data


def data(driver, config):
    for num in range(3):

        name_xp, fw_xp, xp, class_xp, count = '', '', '', '', num + 1

        if count == 1:
            name_xp, fw_xp = config.mixed_name_xp, config.mixed_fw_xp
            calendar_xp, xp = config.mixed_calendar_xp, config.mixed_xp
            class_xp = config.mixed_class_xp
        elif count == 2:
            name_xp, fw_xp = config.paper_name_xp, config.paper_fw_xp
            calendar_xp, xp = config.paper_calendar_xp, config.paper_xp
            class_xp = config.paper_class_xp
        elif count == 3:
            name_xp, fw_xp = config.mixed_name_xp, config.mixed_fw_xp
            calendar_xp, xp = config.mixed_calendar_xp, config.mixed_xp
            class_xp = config.mixed_class_xp

        garbage_type = driver.find_element(By.XPATH, name_xp)
        print(f'\nGenerating {garbage_type.text} information')
        inputs.press_button(driver, xp)
        forward_button = driver.find_element(By.XPATH, fw_xp)

        for i in range(6):
            data_table = driver.find_element(By.XPATH, calendar_xp)
            data, class_value = data_table.find_elements(By.TAG_NAME, 'div'), data_table.find_elements(By.TAG_NAME,
                                                                                                       'td')
            days_data, table_data = [], []

            for row in class_value:
                days_data.append(row.accessible_name)

            for row in data:
                if row.get_attribute("class") == class_xp:
                    table_data.append(row.text)

            common_elements = [value for value in days_data if value[-5:-3:].replace(" ", "") in table_data]
            forward_button.click()
            time.sleep(1)

            for element in common_elements:
                separated_words = element.split()
                date = separated_words[1] + ' ' + str(month_to_int(separated_words[3])) + ' ' + separated_words[4]
                if garbage_type.text == 'Mišrios atliekos':
                    trash = 'mixed'
                elif garbage_type.text == 'Antrinės žaliavos (Popierius/plastikas)':
                    trash = 'paper'
                elif garbage_type.text == 'Antrinės žaliavos (Stiklas)':
                    trash = 'glass'
                writer(config, trash, date)
        print(f'Complete write {garbage_type.text}')


def input_street(driver, config):
    print('Generating street information')
    inputs.home_input(driver, config.street_xp, config.street_name)
    print('Generating hause information')
    inputs.home_input(driver, config.house_xp, config.house_name)


from googleapiclient.http import MediaFileUpload
import os


def upload_json_file_to_drive(service, folder_id, file_path):
    # Extract the file name from the file path
    file_name = os.path.basename(file_path)

    # Search for the file with the given name in the specified folder
    query = f"'{folder_id}' in parents and name='{file_name}' and mimeType='application/json' and trashed=false"
    response = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = response.get('files', [])

    # If the file exists, update it
    if files:
        file_id = files[0]['id']
        media = MediaFileUpload(file_path, mimetype='application/json')
        updated_file = service.files().update(fileId=file_id, media_body=media).execute()
        print(f"File updated successfully. File ID: {updated_file.get('id')}")

    # If the file doesn't exist, create a new one
    else:
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, mimetype='application/json')
        new_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded successfully. File ID: {new_file.get('id')}")


# def download_json_file_from_drive(service, file_id, destination):
#     request = service.files().get_media(fileId=file_id)
#     fh = io.FileIO(destination, 'wb')
#     downloader = MediaIoBaseDownload(fh, request)
#
#     done = False
#     while done is False:
#         status, done = downloader.next_chunk()
#         print(f"Download progress: {int(status.progress() * 100)}%")
#     print(f"File downloaded to {destination}")
