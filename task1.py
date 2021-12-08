# Task 1
# Files
# Write a script that creates a new output file called myfile.txt and
# writes the string "Hello file world!" in it. Then write another script that opens myfile.txt,
# and reads and prints its contents. Run your two scripts from the system command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.

# Завдання 1
# Файли
# Напишіть сценарій, який створює новий вихідний файл під назвою myfile.txt
# і записує рядок "Hello file world!" у цьому. Потім напишіть інший сценарій, який відкриває myfile.txt,
# читає та друкує його вміст. Запустіть два сценарії з системного командного рядка.
# Чи відображається новий файл у каталозі, де ви запускали свої сценарії?
# Що робити, якщо додати інший шлях до каталогу до імені файлу, переданого для відкриття?
# Примітка: методи запису файлів не додають символи нового рядка до ваших рядків;
# додайте явний ‘\n’ в кінець рядка, якщо ви хочете повністю завершити рядок у файлі.


def read_from_file(file_name):
    try:
        with open(file_name) as opened_file:
            k = opened_file.read()
            print(k)
    except FileNotFoundError:
        print("File not found!")


def write_to_file(data, file_name):
    with open(file_name, 'a') as opened_file:
        opened_file.write(data)


status = True
while status:
    user_file_name = input("Enter file name: ")
    what_to_do = input('You wont read from file or wrinte to file?[r\w]\n[q]-exit: ')
    if what_to_do == "q" or what_to_do == 'Q':
        status = False
        exit()
    elif what_to_do == "w":
        user_str_data = input("What you wont to write?: ")
        write_to_file(user_str_data, user_file_name)
    read_from_file(user_file_name)
