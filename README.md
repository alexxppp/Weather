# WeatherApp
#### Video Demo: https://youtu.be/hrTs9wnCeas?feature=shared
#### Description:

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
- [API Integration](#api-integration)
- [Database Schema](#database-schema)
- [Logging](#logging)
- [Security Considerations](#security-considerations)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

## Introduction
WeatherApp is a user-friendly application that allows you to check the current temperature of any location worldwide. Whether you're planning a trip, curious about the weather in a random city, or just need to check your local forecast, WeatherApp has you covered. Leveraging the power of the WeatherAPI, this app provides real-time weather data with just a few clicks.

## Features
This app includes several key features designed to enhance the user experience:

- **User-friendly Menu:** Navigate through the app with ease using a simple and intuitive menu. Options include:
  - Consult current weather for any location.
  - Add or remove favorite locations.
  - Log out of your session.
  - Exit the application.

- **User Registration and Login:**
  - Securely register with a unique username and password. Passwords are hashed using the Werkzeug library to ensure security.
  - Login functionality allows returning users to access their saved favorite locations.

- **Favorite Locations:**
  - Save frequently checked locations to your favorites list for quick access.
  - Your favorite locations are displayed automatically each time you log in.

- **"I'm Feeling Lucky" Feature:**
  - Curious about the weather in a random part of the world? Use the "I'm Feeling Lucky" option to get the weather for a random location selected from over 7,000 cities worldwide.

- **Automatic Terminal Clearing:**
  - For better displayablity and design, the terminal clear itself after some key requests to keep it simple and clean using the os library

- **Error Handling:**
  - Comprehensive error handling ensures that invalid inputs and failed API requests are managed gracefully, providing a smooth user experience.

## Technologies Used
- **Backend:** Python, SQLite
- **API:** WeatherAPI.com
- **Libraries:**
  - **requests:** For making HTTP requests to the WeatherAPI.
  - **Werkzeug:** For password hashing and verification.
  - **cs50:** For interacting with the SQLite database.
  - **geonamescache:** For generating random city names.
- **Testing:** Pytest

## Configuration
The app is highly configurable, allowing you to tailor it to your needs:
- **API Configuration:**
  - Modify the API key and parameters in the `fetch` function to customize the data retrieved from WeatherAPI.
- **Password Management:**
  - Adjust the password length and complexity in the `generate_password` function to meet your security requirements.

## API Integration
WeatherApp integrates with the WeatherAPI to retrieve real-time weather data. The `fetch` function sends requests to the API and parses the JSON response to display the current temperature in the specified location. The app handles API errors and invalid locations gracefully, ensuring that users receive clear feedback.

## Database Schema
WeatherApp uses an SQLite database (`weather.db`) to store user data and favorite locations. The schema includes:
- **Users Table:** Stores usernames and hashed passwords.
- **Favorites Table:** Stores usernames and their associated favorite locations.

This simple schema enables efficient storage and retrieval of user-specific data.

## Logging
WeatherApp employs Python's built-in logging module to manage log levels and suppress unnecessary debug output from external libraries like `requests` and `urllib3`. This keeps the terminal output clean and focused on user-relevant information.

## Security Considerations
- **Password Hashing:** User passwords are securely hashed using Werkzeug, ensuring that plain-text passwords are never stored in the database.
- **Input Validation:** All user inputs are validated to prevent SQL injection and other forms of malicious input. The app handles unexpected inputs and errors gracefully.

## Testing
Testing is an integral part of the development process. To ensure the app functions correctly, run tests using Pytest:
- **Unit Tests:** Test individual functions and modules to ensure they behave as expected.

To run the tests, execute the following command:
```bash
pytest test_weather_app.py
```
All tests should pass, confirming that the application is functioning as expected.

## Future Enhancements

While WeatherApp is fully functional, there is one key improvement that can be made:

- **Extended Weather Data:** Display additional weather information such as humidity, wind speed, and weather conditions.

## Conclusion

WeatherApp is a robust and user-friendly tool for checking the weather in any location worldwide. With features like user authentication, favorite locations, and random location selection, it offers a comprehensive and enjoyable user experience. The app's simple configuration, strong security measures, and comprehensive error handling make it both reliable and easy to use.

Feel free to explore, enhance, and expand the WeatherApp to meet your specific needs. Happy coding!
