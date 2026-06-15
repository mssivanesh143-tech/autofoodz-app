import flet as ft
from datetime import datetime

prices = {
    "Biryani": 150,
    "Dosa": 50,
    "Pizza": 200,
    "Burger": 120,
    "Idli": 40
}

order_history = []

def main(page: ft.Page):
    page.title = "AUTOFOODZ"
    page.bgcolor = "#FF6B00"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Title
    title = ft.Text("🍕 AUTOFOODZ Mobile App", size=26,
                    weight=ft.FontWeight.BOLD, color="white")

    # Inputs
    name_input = ft.TextField(label="Your Name", bgcolor="white")
    food_dropdown = ft.Dropdown(
        label="Choose Food",
        bgcolor="white",
        options=[ft.dropdown.Option(f) for f in prices.keys()]
    )
    qty_input = ft.TextField(
        label="Quantity",
        bgcolor="white",
        keyboard_type=ft.KeyboardType.NUMBER,
        value="1"
    )

    result = ft.Text("", color="white", size=16)
    summary = ft.Column([])
    history_list = ft.Column([])

    def place_order(e):
        name = name_input.value
        food = food_dropdown.value
        qty = qty_input.value

        if not name or not food or not qty:
            result.value = "⚠️ Fill all fields!"
            page.update()
            return

        total = prices[food] * int(qty)
        time_now = datetime.now().strftime("%I:%M %p")

        # Save to history
        order_history.append({
            "name": name,
            "food": food,
            "qty": qty,
            "total": total,
            "time": time_now
        })

        result.value = f"✅ Order placed for {name}!"

        # Order summary
        summary.controls = [
            ft.Container(
                bgcolor="white",
                border_radius=10,
                padding=15,
                content=ft.Column([
                    ft.Text("🧾 Order Summary",
                            weight=ft.FontWeight.BOLD,
                            color="#FF6B00", size=18),
                    ft.Text(f"👤 Name  : {name}", color="#333333"),
                    ft.Text(f"🍽️ Food  : {food}", color="#333333"),
                    ft.Text(f"🔢 Qty   : {qty}", color="#333333"),
                    ft.Text(f"💰 Price : ₹{prices[food]} each",
                            color="#333333"),
                    ft.Divider(color="#FF6B00"),
                    ft.Text(f"💵 Total : ₹{total}",
                            weight=ft.FontWeight.BOLD,
                            color="#FF6B00", size=20),
                ])
            )
        ]

        # Order history
        history_list.controls = [
            ft.Text("📋 Order History",
                    weight=ft.FontWeight.BOLD,
                    color="white", size=20),
            *[
                ft.Container(
                    bgcolor="white",
                    border_radius=8,
                    padding=10,
                    margin=5,
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"#{i+1} {o['food']}",
                                    weight=ft.FontWeight.BOLD,
                                    color="#FF6B00"),
                            ft.Text(f"👤 {o['name']} | 🔢 {o['qty']}",
                                    color="#333333", size=12),
                        ], expand=True),
                        ft.Column([
                            ft.Text(f"₹{o['total']}",
                                    weight=ft.FontWeight.BOLD,
                                    color="#FF6B00"),
                            ft.Text(f"🕐 {o['time']}",
                                    color="#999999", size=11),
                        ])
                    ])
                )
                for i, o in enumerate(order_history)
            ]
        ]

        page.update()

    # Clear history
    def clear_history(e):
        order_history.clear()
        history_list.controls = []
        result.value = "🗑️ History cleared!"
        page.update()

    order_btn = ft.FilledButton(
        content=ft.Text("Place Order 🛒", color="#FF6B00"),
        on_click=place_order,
        style=ft.ButtonStyle(bgcolor="#FFFFFF")
    )

    clear_btn = ft.FilledButton(
        content=ft.Text("Clear History 🗑️", color="white"),
        on_click=clear_history,
        style=ft.ButtonStyle(bgcolor="#CC0000")
    )

    page.add(
        ft.Column([
            title,
            name_input,
            food_dropdown,
            qty_input,
            ft.Row([order_btn, clear_btn]),
            result,
            summary,
            ft.Divider(color="white"),
            history_list
        ])
    )

ft.app(target=main,view=ft.AppView.WEB_BROWSER)