# BorrowBox App Demo

## Project Overview

**BorrowBox** is a front-end prototype for a community-based rental platform designed to help dorm residents share commonly needed items, such as vacuum cleaners, gaming consoles, and car snow scrapers. The idea behind BorrowBox is to provide an easy and efficient way for students to access items they only need occasionally without the burden of ownership, fostering a more sustainable and cost-effective environment. In this demo, users can log in, browse available items, book them for a specific duration, and receive an access code to pick them up from a designated location.

### Business Context
This project was part of my *ENTI 201: Introduction to Business Venturing* course at the University of Calgary, where we were tasked with creating a business venture and a corresponding app prototype. The goal was to quickly develop an application that illustrated the concept of our business idea, BorrowBox, without the need for backend services or a database. This demo focuses solely on the front-end user interface and its functionality.

## Goal of BorrowBox

BorrowBox aims to solve the common problem of over-consumption and clutter in dorms by providing an easy platform for borrowing essential items. Rather than owning items that are rarely used, students can access them for a small rental fee. The app is designed to be user-friendly, allowing students to quickly browse available items, select a rental duration, and complete the booking process. Ultimately, BorrowBox helps reduce unnecessary expenses, promote sharing within the dormitory community, and foster responsible consumption.

## Tool Used: NiceGUI

This project was developed using **NiceGUI**, a Python library that simplifies front-end development by allowing developers to build interactive user interfaces purely in Python. Unlike traditional web development where HTML, CSS, and JavaScript are required, NiceGUI enables the creation of modern web applications with minimal setup and coding.

NiceGUI is built on top of *FastAPI*, and it provides a straightforward, declarative syntax to design UI components like buttons, input fields, images, and more. By using NiceGUI, I was able to quickly prototype the user interface for BorrowBox without needing to learn or use additional front-end technologies. It allows Python developers to focus on logic while creating beautiful, functional web interfaces, making it ideal for rapid application development.

Key features of NiceGUI:
- **Declarative UI Components**: UI elements like buttons, input fields, and images are defined in Python, simplifying the process of constructing a web interface.
- **Real-Time Updates**: Components can be dynamically updated in response to user actions.
- **Built on FastAPI**: For handling HTTP requests efficiently and integrating with backend services (if needed).

### Key UI Features of BorrowBox:
- **Login Page**: Users can log into the app with a username and password.
- **Booking Page**: Users can browse and select available items to rent.
- **Duration Selection**: Users can choose the rental duration based on available time slots.
- **Payment Page**: Mock payment form to simulate the booking process.
- **Access Code Page**: After completing the payment, an access code is generated for the user to pick up the rented item.

## Future Improvements

While this demo only showcases the front-end of the BorrowBox app, the following improvements could be made in the future:

- **Backend Integration**: Integrating a database to store user data, item availability, and booking history.
- **User Authentication**: Implementing more secure user authentication using OAuth or JWT tokens.
- **Payment Gateway**: Adding real payment processing with services like Stripe or PayPal.
- **Advanced Item Availability**: Implementing a dynamic scheduling system to handle item availability based on real-time data.
- **Mobile App Version**: Converting the app into a mobile version using frameworks like Kivy or React Native.

## Conclusion

This project serves as a prototype for the BorrowBox concept, providing a glimpse into how the application could look and function. By using NiceGUI for development, I was able to rapidly create a user interface in Python, making it easy to demonstrate the potential of BorrowBox. While this demo lacks full backend functionality, it effectively illustrates the core features of the app and its user flow.

## How to Use This Repo

- Python 3.7 or higher
- Install required Python packages by running the following command:
  
  ```bash
  pip install -r requirements.txt
# Running the Application

## Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/BorrowBox-App-Demo.git
cd BorrowBox-App-Demo 

# Run the Application
python main.py
