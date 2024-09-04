import src.classes_wrapper as classes
import yaml
import sys

path = sys.path


def garbage_class(yml):
    with open(yml, encoding='utf8') as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
    paper_name_xp = my_config['garbages']['paper']['name_xpath']
    paper_calendar_xp = my_config['garbages']['paper']['calendar_xpath']
    paper_class_xp = my_config['garbages']['paper']['class_xpath']
    glass_name_xp = my_config['garbages']['glass']['name_xpath']
    glass_calendar_xp = my_config['garbages']['glass']['calendar_xpath']
    glass_class_xp = my_config['garbages']['glass']['class_xpath']
    mixed_name_xp = my_config['garbages']['mixed']['name_xpath']
    mixed_calendar_xp = my_config['garbages']['mixed']['calendar_xpath']
    mixed_class_xp = my_config['garbages']['mixed']['class_xpath']
    return classes.GarbageClass(paper_name_xp, paper_calendar_xp, paper_class_xp,
                                glass_name_xp, glass_calendar_xp, glass_class_xp,
                                mixed_calendar_xp, mixed_class_xp, mixed_name_xp
                                )


def address_class(yml):
    with open(yml, encoding='utf8') as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
    street_xp = my_config['street']['xpath']
    street_name = my_config['street']['name']
    house_xp = my_config['house']['xpath']
    house_name = my_config['house']['name']
    return classes.AddressClass(street_xp, street_name, house_xp, house_name)


def buttons_class(yml):
    with open(yml, encoding='utf8') as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
    paper_xp = my_config['buttons']['paper_xpath']
    glass_xp = my_config['buttons']['glass_xpath']
    mixed_xp = my_config['buttons']['mixed_xpath']
    paper_fw_xp = my_config['buttons']['paper_fw_xpath']
    glass_fw_xp = my_config['buttons']['glass_fw_xpath']
    mixed_fw_xp = my_config['buttons']['mixed_fw_xpath']
    return classes.ButtonsClass(paper_xp, glass_xp,
                                paper_fw_xp, glass_fw_xp,mixed_fw_xp, mixed_xp
                                )


def api_class(yml):
    with open(yml, encoding='utf8') as f:
        my_config = yaml.load(f, Loader=yaml.FullLoader)
    token = my_config['api']['token']
    credentials = my_config['api']['credentials']
    folder_id = my_config['api']['folder_id']
    file_path = my_config['api']['file_path']
    writer_scope = my_config['api']['writer_scope']
    reader_scope = my_config['api']['reader_scope']
    return classes.ApiClass(token, credentials, folder_id,
                            file_path, writer_scope, reader_scope)


garbage_configs = garbage_class(f'{path[1]}/config/main.yml')
button_configs = buttons_class(f'{path[1]}/config/main.yml')
api_configs = api_class(f'{path[1]}/config/main.yml')
address_configs = address_class(f'{path[1]}/config/main.yml')
