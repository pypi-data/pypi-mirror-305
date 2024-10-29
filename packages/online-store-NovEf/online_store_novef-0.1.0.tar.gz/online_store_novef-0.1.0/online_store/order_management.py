class OrderManager:
    def __init__(self):
        #Initialization dictionary for saving orders
        self.order_dict = {}

    def create_order(self, order_id, order_data):
        #Add order
        if order_id not in self.order_dict.keys():
            self.order_dict[order_id] = order_data
            return f"Заказ с ID <{order_id}> добавлен"
        return f"Заказ с ID <{order_id}> уже существует"

    def update_order(self, order_id, order_data):
        #Update order
        if order_id in self.order_dict.keys():
            self.order_dict[order_id] = order_data
            return f"Заказ с ID <{order_id}> обновлен"
        return f"Заказ с ID <{order_id}> не найден"

    def cancel_order(self, order_id):
        #Cancel order
        if order_id in self.order_dict.keys():
            del self.order_dict[order_id]
            return f"Заказ с ID <{order_id}> отменен"
        return f"Заказ с ID <{order_id}> не найден"