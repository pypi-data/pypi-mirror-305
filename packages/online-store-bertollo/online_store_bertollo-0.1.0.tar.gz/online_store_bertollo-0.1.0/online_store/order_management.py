class OrderManager:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, order_data):
        if self.orders.get(order_id) is not None:
            print(f"Заказ с ID {order_id} уже существует")
            return
        self.orders[order_id] = order_data
        print(f"Заказ с ID {order_id} добавлен")

    def update_order(self, order_id, order_data):
        if self.orders.get(order_id) is None:
            print(f"Заказ с ID {order_id} не найден")
            return
        for k, v in order_data.items():
            self.orders[order_id][k] = v
        print(f"Заказ с ID {order_id} обновлён")

    def cancel_order(self, order_id):
        if self.orders.get(order_id) is None:
            print(f"Заказ с ID {order_id} не найден")
            return
        del self.orders[order_id]
        print(f"Заказ с ID {order_id} отменён")
