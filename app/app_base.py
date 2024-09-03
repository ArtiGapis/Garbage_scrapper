
read_api = api.authenticate(config.api_configs, config.api_configs.writer_scope)

# Local path where you want to save the downloaded JSON file
destination = 'downloaded_file.json'
file_id = '1cQLhSkppMyKvJ0hij3otK3TKRPctkw1U'
# Download the JSON file from Google Drive
works.download_json_file_from_drive(read_api, file_id, destination)