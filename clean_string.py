def clean_string(input_file, output_file):
    # Читаем файл
    with open(input_file, 'r') as f:
        content = f.read()

    # Удаляем все скобки, запятые, пробелы и переносы строк
    cleaned_content = content.replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\n', '')

    # Заменяем 'm0' и '[33m0' на '0' (обнаружены в данных)
    cleaned_content = cleaned_content.replace('m0', '0').replace('[33m0', '0')

    # Записываем результат в новый файл
    with open(output_file, 'w') as f:
        f.write(cleaned_content)

    print(f"Обработанные данные сохранены в {output_file}")
    print(f"Длина строки: {len(cleaned_content)} символов")


# Использование функции
clean_string('message(1).txt', 'cleaned_data.txt')