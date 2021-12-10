# Розширити додаток Телефонна книга
# Функціональність програми «Телефонна книга»:
# Додайте нові записи
# Шукати по імені
# Шукати за прізвищем
# Шукати за повним іменем
# Пошук за номером телефону
# Пошук за містом або штатом
# Видалити запис для заданого номера телефону
# Оновити запис для заданого номера телефону
# Можливість виходу з програми
#
# Першим аргументом програми має бути назва телефонної книги.
# Програма повинна завантажувати дані JSON,
# якщо вони присутні в папці з програмою, інакше виникне помилка.
# Після виходу користувача всі дані повинні бути збережені в завантаженому JSON.
import datetime
import json
import io


def check_user_data():
    status = True
    while status:
        name = input("Enter name subscriber: ").strip().capitalize()
        surname = input("Enter surname subscriber: ").strip().capitalize()
        city = input("Enter city subscriber: ").strip().capitalize()
        m_phone = input("Enter mobile  phone subscriber[press Enter If not]: ")
        h_phone = input("Enter home  phone subscriber[press Enter If not]: ")
        phones_dict = {"mobile": m_phone,
                       "home": h_phone}
        if len(name) <= 3 and len(surname) <= 3 and len(city) <= 3 and phones_dict["mobile"].__contains__("+380"):
            print(
                "Сheck the entered data. name and surname must contain more than 3 characters.And mobile phone must contain [+380]")
            continue
    status = False
    return name, surname, city, phones_dict


# def add_new_entries():
#     data = {
#         "name": None,
#         "surname": None,
#         "city": None,
#         "street": None,
#         "account creation date": datetime.datetime.now().strftime("%d/%m/%y"),
#         "phones": {
#             "mobile": None,
#             "home": None
#         }
#
#     }
#     for i in data:
#         data["name"] = us_name
#         data["surname"] = us_surname
#         data["city"] = city
#         data["street"] = street
#         data["phones"] = kwargs


def search_by_first_name():
    us_ent_name = input("Enter name:")
    with open("telephone_book.json", "r") as opened_file:
        j_phone_book = json.load(opened_file, )
        print(type(j_phone_book))
        for i in j_phone_book:
            if i["name"] == us_ent_name:
                print(i)


def search_by_last_name():
    us_ent_surname = input("Enter surname:")
    with open("telephone_book.json") as opened_file:
        j_phone_book = json.load(opened_file)
        for i in j_phone_book:
            if i["surname"] == us_ent_surname:
                print(i)
    pass


def search_by_full_name():
    pass


def search_by_telephone_number():
    pass


def search_by_city_or_state():
    pass


def delete_a_recoder_for_a_given_telephone_number():
    pass


def update_a_recoder_for_a_given_telephone_number():
    pass


sym = "-"
print(sym * 5, "Hello at my phone book", sym * 5)
answers = ("1", "2", "3", "4", "5", "6", '7')
ans = ""
while ans not in answers:
    ans = input("\n1-Search by first name"
                "\n2-Search by surname name"
                "\n3-Search by full name"
                "\n4-Search by telephone number"
                "\n5-Search by city"
                "\n6-Add new user"
                "\n7-Delete user "
                "\nChoose what you wont:")

if ans == "1":
    first_name = input("Enter the name: ")
    search_by_first_name(first_name)
elif ans == "2":
    search_by_last_name()
elif ans == "3":
    search_by_full_name()
elif ans == '4':
    search_by_telephone_number()
elif ans == "5":
    search_by_city_or_state()
elif ans == "6":
    pass
else:
    delete_a_recoder_for_a_given_telephone_number()
# di_ans = {"1": search_by_first_name(),
#           "2": search_by_last_name(),
#           "3": search_by_full_name(),
#           "4": search_by_telephone_number(),
#           "5": search_by_city_or_state(),
#           "6": "add",
#           "7": delete_a_recoder_for_a_given_telephone_number()
#           }
# for i in di_ans.values():
#     if ans == i:
#         di_ans[ans]
