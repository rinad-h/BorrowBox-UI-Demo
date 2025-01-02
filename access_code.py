import random
from nicegui import app, ui

# Access code page (after payment)
@ui.page('/access_code')
def access_code_page() -> None:
    def generate_access_code() -> str:
        return ''.join(random.choices(string.digits, k=6))

    access_code = generate_access_code()
    app.storage.user['access_code'] = access_code

    with ui.column().classes('absolute-center items-center'): 
        ui.label('Your Access Code').classes('text-2xl mb-4') 
        ui.label(access_code).classes('text-6xl mb-4 text-center').props('style="font-weight: bold; color: #ff9900;"') 
        ui.label('Please input this code at the start of your time slot.') 
        ui.label('The machine is located in the lobby of the dorms at University of Calgary, Rundle Hall')
