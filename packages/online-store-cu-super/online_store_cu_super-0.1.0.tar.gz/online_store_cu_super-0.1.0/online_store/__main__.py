from my_project.online_store import UserManager, OrderManager

user_manager = UserManager()
order_manager = OrderManager()

def main_menu():
    while True:
        print('\nВыберите действие:')
        print('1. Управление учетными записями')
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
    while True:
        print('\nУправление учетными записями клиентов:')
        print('1. Добавить учетную запись')
        print('2. Найти учетную запись')
        print('3. Удалить учетную запись')
        print('4. Назад')
        choice = input('Выберите действие: ')
        if choice == '1':
            user_id = input('Введите email клиента: ')
            name = input('Введите имя: ')
            age = int(input('Введите возраст: '))
            user_manager.add_user(user_id, {'name': name, 'age': age})
        elif choice == '2':
            user_id = input('Введите email клиента: ')
            user_data = user_manager.find_user(user_id)
            if user_data:
                print(f'Найден клиент: {user_data}')
        elif choice == '3':
            user_id = input('Введите email клиента: ')
            user_manager.remove_user(user_id)
        elif choice == '4':
            return
        else:
            print('Некорректный ввод.')

def order_menu():
    while True:
        print('\nУправление заказами:')
        print('1. Создать заказ')
        print('2. Обновить заказ')
        print('3. Отменить заказ')
        print('4. Назад')
        choice = input('Выберите действие: ')
        if choice == '1':
            order_id = input('Введите ID заказа: ')
            user_id = input('Введите учетную запись клиента: ')
            item = input('Введите товар: ')
            price = float(input('Введите цену: '))
            order_manager.create_order(order_id, {'user_id': user_id, 'item': item, 'price': price})
        elif choice == '2':
            order_id = input('Введите ID заказа: ')
            new_data = input('Введите новые данные заказа (в формате "item,price"): ').split(',')
            order_manager.update_order(order_id, {'item': new_data[0], 'price': float(new_data[1])})
        elif choice == '3':
            order_id = input('Введите ID заказа: ')
            order_manager.cancel_order(order_id)
        elif choice == '4':
            return
        else:
            print('Некорректный ввод.')

if __name__ == '__main__':
    main_menu()