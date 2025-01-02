from nicegui import app, ui
from routes_select_duration import select_duration_page

# Booking page (after login)
@ui.page('/booking')
def booking_page() -> None:
    # Function to handle booking selection and redirect to duration page
    def show_item_details(item: str) -> None:
        app.storage.user['selected_item'] = item
        ui.navigate.to('/select_duration')  # Redirect to the duration selection page

    # List of items to be displayed
    items = [
        {"name": "Vacuum", "image": "https://picsum.photos/id/377/640/360"},  # Replace with real image URLs
        {"name": "Steamer", "image": "https://picsum.photos/id/377/640/360"},
        {"name": "Nintendo Switch", "image": "https://picsum.photos/id/377/640/360"},
        {"name": "Car Snow Scraper", "image": "https://picsum.photos/id/377/640/360"}
    ]

    with ui.column().classes('absolute-center items-center'):
        ui.label('Select an item to book').classes('text-xl mb-4')

        # Display list of items
        for item in items:
            with ui.row().classes('mb-4 items-center'):
                # Button to show item details on click
                ui.button(item["name"], on_click=lambda item=item: show_item_details(item["name"])).classes('w-full')

    return None
