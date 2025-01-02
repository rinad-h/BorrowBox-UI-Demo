import random
import string
from typing import Optional
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from nicegui import app, ui
from middleware_auth import AuthMiddleware
from routes_login import login_page
from routes_booking import booking_page
from routes_select_duration import select_duration_page
from routes_payment import payment_page
from routes_access_code import access_code_page

# Dummy user data (in a real application, passwords should be hashed)
passwords = {'user1': 'pass1', 'user2': 'pass2'}

# Pages that don't require authentication
unrestricted_page_routes = {'/login'}

class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.
    It redirects the user to the login page if they are not authenticated.
    """
    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if not request.url.path.startswith('/_nicegui') and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)

app.add_middleware(AuthMiddleware)

# Main page - after login
@ui.page('/')
def main_page() -> None:
    def logout() -> None:
        app.storage.user.clear()
        ui.navigate.to('/login')

    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        ui.button(on_click=logout, icon='logout').props('outline round')
        
        # Button to navigate to the booking page
        ui.button('Go to Booking', on_click=lambda: ui.navigate.to('/booking'))
