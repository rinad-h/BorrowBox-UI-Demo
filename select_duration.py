import random
from nicegui import app, ui
from routes_payment import payment_page

# Duration selection page (after booking an item)
@ui.page('/select_duration')
def select_duration_page() -> None:
    # Function to handle booking duration selection and redirect to the payment page
    def confirm_booking() -> None:
        item = app.storage.user.get('selected_item', 'Unknown')
        selected_times = [i for i in range(24) if selected_hours[i]]
        total_hours = len(selected_times)
        if item == "Vacuum":
            total_cost = total_hours * 5  # $5 per hour for Vacuum
        else:
            total_cost = total_hours * 3  # $3 per hour for other items
        app.storage.user.update({'total_cost': total_cost, 'selected_times': selected_times})
        ui.navigate.to('/payment')  # Redirect to the payment page

    item = app.storage.user.get('selected_item', 'No item selected')

    # Randomly generate availability for 24 hours (red = unavailable, green = available)
    availability = [random.choice(['green', 'red']) for _ in range(24)]

    # Track selected hours
    selected_hours = [False] * 24

    # Create UI elements for selected times and total cost
    selected_times_label = ui.label().classes('mt-4 text-lg')
    total_cost_label = ui.label().classes('mt-2 text-lg')

    def update_labels():
        # Display selected hours at the bottom
        selected_times = [str(i) + ':00' for i in range(24) if selected_hours[i]]
        selected_times_label.text = f'Selected times: {", ".join(selected_times)}'

        # Display the total cost
        total_hours = len([i for i in range(24) if selected_hours[i]])
        if item == "Vacuum":
            total_cost = total_hours * 5  # $5 per hour for Vacuum
        else:
            total_cost = total_hours * 3  # $3 per hour for other items
        total_cost_label.text = f'Total Cost: ${total_cost}'

    def select_hour(hour=0):
        """Toggles hour selection between green (available) and yellow (selected)"""
        if availability[hour] == 'green':  # Only allow selection if the time slot is green
            selected_hours[hour] = not selected_hours[hour]  # Toggle selected status
            button = hour_buttons[hour]
            button.props(f'color={"yellow" if selected_hours[hour] else "green"}')
            update_labels()

    hour_buttons = []

    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Select booking duration for {item}').classes('text-xl mb-4')

        # Display 24 hours horizontally
        with ui.row().classes('wrap justify-center'):
            for hour in range(24):
                # Set color based on availability
                color = 'green' if availability[hour] == 'green' else 'red'

                # Button for each hour
                button = ui.button(f'{hour}:00', on_click=lambda hour=hour: select_hour(hour))
                button.props(f'color={color}')
                button.classes('mx-1')
                hour_buttons.append(button)

        # Add the labels for selected times and total cost
        update_labels()

        # Display the labels for selected times and total cost
        with ui.column():
            selected_times_label.classes('mt-4 text-lg')
            total_cost_label.classes('mt-2 text-lg')

        # Confirm booking button
        ui.button('Confirm Booking', on_click=confirm_booking).classes('mt-4 text-lg')
