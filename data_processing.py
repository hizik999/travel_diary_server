from pathlib import Path
import csv

motion_txt_path = "useful_dataset/motion.txt"
label_txt_path = "useful_dataset/label.txt"

folder_path_string = "full_archive/release/User1/"
folder_path = Path(folder_path_string)

hips_motion = "Hips_Motion.txt"
label = "Label.txt"

### очистка содержимого в файлах
with open(motion_txt_path, 'w') as motion_file:
    pass

with open(label_txt_path, 'w') as label_file:
    pass

### перебор всех папок в User1/
for file_name in folder_path.iterdir():
    folder_name = str(file_name).split("/")[-1]
    try:
        for file in file_name.iterdir():
            last_file_name = str(file).split("/")[-1]
            if last_file_name == hips_motion:
                with open(file, 'r') as source_file:
                    with open(motion_txt_path, 'a') as motion_file:
                        source_data = source_file.readlines()
                        for line in source_data:
                            motion_file.write(line)
            elif last_file_name == label:
                with open(file, 'r') as source_file:
                    with open(label_txt_path, 'a') as label_file:
                        source_data = source_file.readlines()
                        for line in source_data:
                            label_file.write(line)
    except:
        print(folder_name + " not a directory")
    print("processed", folder_name)

print('finished!')


####################################################################################


label_csv_path = "useful_dataset/label.csv"

# Открываем текстовый файл для чтения
with open(label_txt_path, 'r') as txt_file:
    # Читаем строки из текстового файла
    lines = txt_file.readlines()

# Определяем заголовки столбцов
headers_label = ['time', 'coarse', 'fine_label', 'road_label', 'traffic_label', 'tunnels_label', 'social_label', 'food_label']

# Открываем CSV файл для записи
with open(label_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Записываем заголовки
    csv_writer.writerow(headers_label)

    # Записываем данные из текстового файла
    for line in lines:
        # Разбиваем каждую строку по пробелам (или другим разделителям, если нужно)
        row = line.strip().split()
        csv_writer.writerow(row)

print("Файл успешно преобразован в CSV.")
