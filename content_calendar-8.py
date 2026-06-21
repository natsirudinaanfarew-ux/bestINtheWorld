# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ContentCalendar
def print_menu():
    print("\n=== Меню действий ===")
    print("1. Добавить публикацию")
    print("2. Удалить публикацию")
    print("3. Изменить статус публикации")
    print("4. Показать все каналы")
    print("5. Выход")

def get_int_menu():
    while True:
        try:
            choice = input("\nВведите номер действия (1-5): ")
            if choice in ["1", "2", "3", "4", "5"]:
                return int(choice)
            print("Неверный выбор.")
        except ValueError:
            print("Ошибка ввода. Введите число от 1 до 5.")

def main():
    while True:
        print_menu()
        choice = get_int_menu()
        if choice == 1:
            pub_id = input("ID публикации (или Enter для авто): ") or len(posts) + 1
            title = input("Заголовок: ")
            channel = input("Канал: ")
            topic = input("Тема: ")
            status = "Черновик"
            idea = input("Идея/Описание: ")
            posts.append({"id": pub_id, "title": title, "channel": channel, "topic": topic, "status": status, "idea": idea})
        elif choice == 2:
            idx = int(input("ID публикации для удаления (или Enter для пропуска): ")) or -1
            if 0 <= idx < len(posts):
                del posts[idx]
        elif choice == 3:
            idx = int(input("ID публикации для изменения статуса: ")) or -1
            if 0 <= idx < len(posts):
                new_status = input("Новый статус (Черновик/В работе/Опубликовано): ")
                posts[idx]["status"] = new_status
        elif choice == 4:
            print("\nКаналы:")
            channels = set(p["channel"] for p in posts)
            for ch in sorted(channels):
                count = sum(1 for p in posts if p["channel"] == ch)
                print(f" - {ch} ({count} публикаций)")
        elif choice == 5:
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()
