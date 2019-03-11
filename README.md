## VKinder
Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок.

Используя данные из VK нужно сделать сервис намного лучше чем Tinder. Искать людей, подходящих под условия, на основании информации о пользователе из VK:
- диапазон возраста,
- пол,
- группы,
- расположение,
- интересы, 
- любой другой необязательный параметр.

У каждого критерия поиска должны быть свои веса. То есть совпадение по возрасту должны быть важнее общих групп. Интересы по музыке важнее книг. Наличие общих друзей важнее возраста.

Разбор похожих интересов(книги, музыка, интересы) нужно будет провести с помощью анализа текста.

У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии с аватара. Популярность  определяется по количеству лайков.

## Входные данные
Имя пользователя или его id в ВК, для которого мы ищем пару.
- если информации недостаточно нужно дополнительно спросить её у пользователя.


## Выходные данные
JSON с 10 объектами, где у каждого объекта перечислены топ-3 фотографии и аккаунт.

## Требование к сервису:
1. Код программы удовлетворяет`PEP8`.
2. Получать токен от пользователя с нужными правами.
3. Программа декомпозирована на функции/классы/модули/пакеты.
4. Результат программы записывать в БД.
5. Люди не должны повторяться при повторном поиске.
6. Реализовать тесты на базовую функциональность.
7. Не запрещается использовать внешние библиотеки для vk.