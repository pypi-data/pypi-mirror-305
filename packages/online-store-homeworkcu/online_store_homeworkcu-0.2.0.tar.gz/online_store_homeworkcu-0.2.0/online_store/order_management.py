class OrderManager:
    def __init__(self):
        self.orders = dict()

    def create_order(self, order_id, order_data):
        if order_id in self.orders:
            print(f'Заказ с ID {order_id} уже существует')
        else:
            self.orders[order_id] = order_data
            print(f'Заказ с ID {order_id} добавлен')

    def update_order(self, order_id, order_data):
        if not(order_id in self.orders):
            print(f'Заказ с ID {order_id} не найден')
        else:
            for i, j in order_data.items():
                self.orders[order_id][i] = j
            print(f'Заказ с ID {order_id} обновлен')

    def cancel_order(self, order_id):
        if not(order_id in self.orders):
            print(f'Заказ с ID {order_id} не найден')
        else:
            self.orders.pop(order_id)
            print(f'Заказ с ID {order_id} отменен')
