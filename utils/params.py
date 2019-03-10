def ask_params():
    user_id = input('Insert your VK ID: ')
    age_from = input('Age from: ')
    age_to = input('Age to: ')
    sex = input('Gender (1 — F, 2 - M, 0 - M and F): ')
    return user_id, sex, age_from, age_to


def ask_missing_params(user):
    updated_data = dict()
    if 'city' not in user.user_data:
        updated_data['city'] = input('City ID: ')
    if 'country' not in user.user_data:
        updated_data['country'] = input('Country ID: ')
    if user.user_data['interests'] is '':
        updated_data['interests'] = input('Insert your interests: ')
    if user.user_data['music'] is '':
        updated_data['music'] = input('Insert your favourite music: ')
    if user.user_data['movies'] is '':
        updated_data['movies'] = input('Insert your favourite movies: ')
    if user.user_data['tv'] is '':
        updated_data['tv'] = input('Insert your favourite tv shows: ')
    if user.user_data['books'] is '':
        updated_data['books'] = input('Insert favourite your books: ')
    return updated_data


def update_params(user):
    missing_params = ask_missing_params(user)
    if missing_params:
        user.update_user_data(missing_params)
