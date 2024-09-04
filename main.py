import src.get_configs as configs
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
works.input_street(chrome, configs.address_configs)

if __name__ == '__main__':
    works.creator(configs.address_configs)
    works.data(chrome, configs)

    write_api = api.authenticate(configs.api_configs, configs.api_configs.writer_scope)

    # Upload the JSON file to Google Drive
    works.upload_json_file_to_drive(write_api, configs.api_configs.folder_id,
                                    configs.api_configs.file_path)

    chrome.quit()
