def serialize_orders_by_user_id(orders):
    joined_orders = []
    for order in orders:
        joined_orders.append(
            {
                "id": order.id,
                "user_id": order.user_id,
                "status": order.status,
                "expires_at": order.expires_at,
                "ticket_id": order.ticket_id,
                "ticket": {
                    "id": order.ticket_id,
                    "title": order.title,
                    "price": order.price,
                },
            }
        )
    return joined_orders
