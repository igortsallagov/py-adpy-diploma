import re
import time
from score.defaults import INTERESTS_SCORE, FRIENDS_SCORE, GROUPS_SCORE, \
                        MUSIC_SCORE, BOOKS_SCORE, TV_SCORE, MOVIES_SCORE, DEFAULT_PATTERN


def check_mutual_friends(users):
    for item in users:
        item.score += FRIENDS_SCORE * item.common_count


def check_mutual_groups(user, users):
    user_groups = set(user.get_groups())
    for position, item in enumerate(users):
        item_groups = set(item.get_groups())
        mutual_groups = user_groups & item_groups
        print(f'Progress: {position + 1}/{len(users)}')
        if mutual_groups:
            item.score += GROUPS_SCORE * len(mutual_groups)
        time.sleep(0.35)


def check_common_interests(user, users):
    pattern = re.sub(DEFAULT_PATTERN, '', user.interests).lower().replace(', ', '|')
    for item in users:
        common_interests = re.findall(pattern, item.interests.lower())
        if common_interests and '' not in common_interests:
            item.score += INTERESTS_SCORE * len(common_interests)


def check_common_music(user, users):
    pattern = re.sub(DEFAULT_PATTERN, '', user.music).lower().replace(', ', '|')
    for item in users:
        common_music = re.findall(pattern, item.music.lower())
        if common_music and '' not in common_music:
            item.score += MUSIC_SCORE * len(common_music)


def check_common_tv(user, users):
    pattern = re.sub(DEFAULT_PATTERN, '', user.tv).lower().replace(', ', '|')
    for item in users:
        common_tv = re.findall(pattern, item.tv.lower())
        if common_tv and '' not in common_tv:
            item.score += TV_SCORE * len(common_tv)


def check_common_movies(user, users):
    pattern = re.sub(DEFAULT_PATTERN, '', user.movies).lower().replace(', ', '|')
    for item in users:
        common_movies = re.findall(pattern, item.movies.lower())
        if common_movies and '' not in common_movies:
            item.score += MOVIES_SCORE * len(common_movies)


def check_common_books(user, users):
    pattern = re.sub(DEFAULT_PATTERN, '', user.books).lower().replace(', ', '|')
    for item in users:
        common_books = re.findall(pattern, item.books.lower())
        if common_books and '' not in common_books:
            item.score += BOOKS_SCORE * len(common_books)


def score_users(user, users):
    print('Checking mutual friends')
    check_mutual_friends(users)
    print('Checking mutual groups')
    check_mutual_groups(user, users)
    print('Checking common interests')
    check_common_interests(user, users)
    print('Checking favourite music')
    check_common_music(user, users)
    print('Checking favourite movies')
    check_common_movies(user, users)
    print('Checking favourite tv shows')
    check_common_tv(user, users)
    print('Checking favourite books')
    check_common_books(user, users)
