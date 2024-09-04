import src.get_configs as config
from chromedriver_py import binary_path
from selenium import webdriver
import src.works_template as works
import src.api_auth as api


# Setting up ChromeDriver service
svc = webdriver.chrome.service.Service(executable_path=binary_path)
# Initializing WebDriver
chrome = webdriver.Chrome(service=svc)
# Navigating to the URL
chrome.get("https://grafikai.svara.lt/")  # Replace with the actual URL
chrome.implicitly_wait(50)
works.input_street(chrome, config.button_configs)

if __name__ == '__main__':
    # works.creator(all_configs)
    # works.data(chrome, all_configs)
    # chrome.quit()

    write_api = api.authenticate(config.api_configs, config.api_configs.writer_scope)

    # Upload the JSON file to Google Drive
    works.upload_json_file_to_drive(write_api, config.api_configs.folder_id,
                                    config.api_configs.file_path)


    # read_api = api.authenticate(config.api_configs, config.api_configs.writer_scope)
    #
    # # Local path where you want to save the downloaded JSON file
    # destination = 'downloaded_file.json'
    # file_id = '1cQLhSkppMyKvJ0hij3otK3TKRPctkw1U'
    # # Download the JSON file from Google Drive
    # works.download_json_file_from_drive(read_api, file_id, destination)

