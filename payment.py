from nicegui import app, ui
from routes_access_code import access_code_page

# Payment page (after confirming the booking)
@ui.page('/payment')
def payment_page() -> None:
    def make_payment() -> None:
        ui.notify('Payment Successful!', color='positive')
        ui.navigate.to('/access_code')  # Redirect to access code page after payment

    total_cost = app.storage.user.get('total_cost', 0)

    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Total amount to pay: ${total_cost}').classes('text-xl mb-4')
        ui.label('Please provide payment details below')

        # Mock payment form (for demo purposes)
        ui.input('Card Number').props('type=text placeholder=Enter your card number')
        ui.input('Expiry Date').props('type=text placeholder=MM/YY')
        ui.input('CVV').props('type=text placeholder=Enter CVV')

        ui.button('Make Payment', on_click=make_payment)
