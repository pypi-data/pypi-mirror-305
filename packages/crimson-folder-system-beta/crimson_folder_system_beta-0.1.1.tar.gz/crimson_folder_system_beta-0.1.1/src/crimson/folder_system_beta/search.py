from crimson.folder_system_beta.filter import Filter, FnFilter
from typing import List, Literal
import os


def search(
    base_root: str,
    filter_obj: Filter = FnFilter(),
    targets: List[Literal["folder", "path"]] = ["folder", "path"],
) -> List[str]:
    search_folders = "folder" in targets
    search_paths = "path" in targets

    results = []

    for root, dirs, files in os.walk(base_root):
        if search_folders:
            for dir_name in dirs:
                results.append(os.path.join(root, dir_name))

        if search_paths:
            for file_name in files:
                results.append(os.path.join(root, file_name))

    return filter_obj.filter(results)
