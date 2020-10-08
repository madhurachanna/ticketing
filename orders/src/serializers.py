def format_datetime(datetime):
    return datetime.strftime("%b %d %Y %H:%M:%S")


def serialize_orders_by_user_id(orders):
    joined_orders = []
    for entry in orders:
        order = entry.Order
        ticket = entry.Ticket
        joined_orders.append(
            {
                "id": order.id,
                "user_id": order.user_id,
                "status": order.status.value,
                "expires_at": format_datetime(order.expires_at),
                "ticket_id": order.ticket_id,
                "ticket": {
                    "id": ticket.id,
                    "title": ticket.title,
                    "price": ticket.price,
                },
            }
        )
    return joined_orders
