from online_store import UserManager, OrderManager

user_manager= UserManager()
order_manager = OrderManager()

def main_menu():
   while True:
       print('\nВыберите действие:')
       print('1. Управление учётными записями')
       print('2. Управление заказами')
       print('3. Выход')

       choice = input('Введите номер действия: ')

       if choice == '1':
           user_menu()
       elif choice == '2':
           order_menu()
       elif choice == '3':
           print('Работа завершена.')
           break
       else:
           print('Некорректный ввод. Попробуйте снова.')


def user_menu():
    print('\nУправление учётными записями клиентов:')
    print('1. Добавить учётную запись')
    print('2. Найти учётную запись')
    print('3. Удалить учётную запись')
    print('4. Назад')

    choice = input('Выберите действие: ')

    if choice == '1':
        user_id = input('Введите email клиента: ')
        name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        # Передаём данные клиента как словарь
        user_data = {'name': name, 'age': age}
        user_manager.add_user(user_id, user_data)

    elif choice == '2':
        user_id = input('Введите email клиента: ')
        user_data = user_manager.find_user(user_id)
        if user_data:
            print(f'Данные клиента: {user_data}')

    elif choice == '3':
        user_id = input('Введите email клиента: ')
        user_manager.remove_user(user_id)

    elif choice == '4':
        return

    else:
        print('Некорректный ввод.')


def order_menu():
    print('\nУправление заказами:')
    print('1. Создать заказ')
    print('2. Обновить заказ')
    print('3. Отменить заказ')
    print('4. Назад')

    choice = input('Выберите действие: ')

    if choice == '1':
        order_id = input('Введите ID заказа: ')
        user = input('Введите учётную запись клиента: ')
        item = input('Введите товар: ')
        price = float(input('Введите цену: '))
        order_data = {
            'user': user,
            'item': item,
            'price': price,
            'status': 'Создан'
        }
        order_manager.create_order(order_id, order_data)

    elif choice == '2':
        order_id = input('Введите ID заказа: ')
        status = input('Введите новый статус заказа: ')
        current_order = order_manager.find_order(order_id)
        if current_order:
            current_order['status'] = status
            order_manager.update_order(order_id, current_order)
        else:
            print(f'Заказ с ID {order_id} не найден')

    elif choice == '3':
        order_id = input('Введите ID заказа: ')
        order_manager.cancel_order(order_id)

    elif choice == '4':
        return

    else:
        print('Некорректный ввод.')

if __name__ == '__main__':
    main_menu()
