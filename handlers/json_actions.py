import json
import aiofiles

async def load_id_list_from_json(file_path: str) -> list:
    """
    Loads the ID list from a JSON file.
    Returns the ID list as a Python list.
    """
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            file_content = await file.read()
            if file_content:
                id_list = json.loads(file_content)
                return id_list
            else:
                return []
    except FileNotFoundError:
        return []

async def save_id_list_to_json(id_list: list, file_path: str) -> None:
    """
    Saves the ID list to a JSON file.
    """
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
        await file.write(json.dumps(id_list))

async def add_id_to_json(id: str, file_path: str) -> None:
    """
    Adds an ID to the JSON file.
    """
    id_list = await load_id_list_from_json(file_path)
    id_list.append(id)
    await save_id_list_to_json(id_list, file_path)

async def remove_id_from_json(id: str, file_path: str) -> None:
    """
    Removes an ID from the JSON file.
    """
    id_list = await load_id_list_from_json(file_path)
    if id in id_list:
        id_list.remove(id)
    await save_id_list_to_json(id_list, file_path)