from typing import Optional
from nicegui import app, ui
from routes_booking import booking_page

# Login page
@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # Local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to('/booking')  # Redirect to booking page after successful login
        else:
            ui.notify('Wrong username or password', color='negative')

    # If the user is already authenticated, redirect to the booking page
    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/booking')

    # Layout for login page
    with ui.column().classes('absolute-center items-center text-center'):
        ui.image(r'C:\Users\rinad\Downloads\Free Simple Modern Circle Design Studio Logo-2.png').style('width: 400px; height: 200px; margin-bottom: 10px;')  # Larger image with less spacing
        ui.label('Welcome to BorrowBox, please log in to your account').style('font-size: 24px; margin-top: 0; text-align: center;')
        # Login form
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)

    return None
