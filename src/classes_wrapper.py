from dataclasses import dataclass


@dataclass()
class GarbageClass:
    paper_name_xp: []
    paper_calendar_xp: []
    paper_class_xp: []
    glass_name_xp: []
    glass_calendar_xp: []
    glass_class_xp: []
    mixed_calendar_xp: []
    mixed_class_xp: []
    mixed_name_xp: []


@dataclass()
class AddressClass:
    street_xp: []
    street_name: []
    house_xp: []
    house_name: []


@dataclass()
class ButtonsClass:
    paper_xp: []
    glass_xp: []
    paper_fw_xp: []
    glass_fw_xp: []
    mixed_fw_xp: []
    mixed_xp: []


@dataclass()
class ApiClass:
    token: []
    credentials: []
    folder_id: []
    file_path: []
    writer_scope: []
    reader_scope: []
