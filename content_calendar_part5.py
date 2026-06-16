# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ContentCalendar
def delete_record(record_id, collection_name):
    if record_id not in records:
        print(f"Ошибка: запись с id {record_id} не найдена в коллекции '{collection_name}'")
        return False
    
    del records[collection_name][record_id]
    print(f"Запись с id {record_id} успешно удалена из коллекции '{collection_name}'")
    return True

def handle_missing_ids(collection_name, missing_ids):
    if not missing_ids:
        return
    
    for record_id in missing_ids:
        if collection_name in records and record_id in records[collection_name]:
            del records[collection_name][record_id]
    
    print(f"Обработано отсутствующих идентификаторов в коллекции '{collection_name}': {missing_ids}")
