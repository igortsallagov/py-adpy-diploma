from config import FIELDS


def ask_params():
    user_id = input('Insert your VK ID: ')
    age_from = input('Age from: ')
    age_to = input('Age to: ')
    sex = input('Gender (1 — F, 2 - M, 0 - M and F): ')
    return user_id, sex, age_from, age_to


def ask_missing_params(user):
    updated_data = dict()
    for item in FIELDS.split(', ')[1:3]:
        if item not in user.user_data:
            updated_data[item] = input(f'{item.capitalize()} ID: ')
    for item in FIELDS.split(', ')[4:]:
        if item not in user.user_data or user.user_data[item] is '':
            if item == 'tv':
                updated_data[item] = input(f'Insert your {item} shows: ')
            else:
                updated_data[item] = input(f'Insert your {item}: ')
    return updated_data


def update_params(user):
    missing_params = ask_missing_params(user)
    if missing_params:
        user.update_user_data(missing_params)
