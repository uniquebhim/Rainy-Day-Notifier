# **Rainy Day Notifier**

Rainy Day Notifier is a Python script that sends an SMS alert to remind you to bring an umbrella if it will rain within the next 12 hours. The script uses the OpenWeatherMap API to retrieve the hourly weather forecast for a specified location, and checks if the forecast includes any precipitation. If precipitation is expected, the script uses the Twilio API to send an SMS message to your phone number with a reminder to bring an umbrella.

## **Getting Started**

### **Prerequisites**

- Python 3.x
- requests module (**`pip install requests`**)
- twilio module (**`pip install twilio`**)

You'll also need to sign up for an account with **[OpenWeatherMap](https://openweathermap.org/)** and **[Twilio](https://www.twilio.com/)** to obtain API keys.

### **Installation**

1. Clone this repository to your local machine.
2. Install the necessary Python modules (see "Prerequisites" above).
3. Replace **`MY_LATITUDE`**, **`MY_LONGITUDE`**, **`WEATHER_API_KEY`**, **`account_sid`**, **`auth_token`**, and phone number in the script with your own values.

### **Usage**

To run the script, navigate to the project directory in your terminal and enter the command:

```
bash code
python rainy_day_notifier.py

```

If precipitation is expected within the next 12 hours, you will receive an SMS alert reminding you to bring an umbrella.

### **Optional: Running the Script Automatically**

If you want the script to run automatically at a certain time every day, you can use the built-in task scheduler on your operating system.

On Windows, you can use Task Scheduler. On macOS and Linux, you can use cron. Here are some example cron commands to run the script at 8:00 AM every day:

```
bash code
0 8 * * * python /path/to/rainy_day_notifier.py

```

## **Contributing**

If you find a bug or want to suggest a feature, please open an issue or submit a pull request. All contributions are welcome!

## **License**

This project is licensed under the **[MIT License](https://opensource.org/licenses/MIT)**.
