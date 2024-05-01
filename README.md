# Smart Refrigerator with Telegram Integration

![Smart Refrigerator](https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/56ac01b0-4330-4071-a7d7-439ccde59e1f)


## Overview

This project is a smart refrigerator system that integrates with Telegram, allowing users to remotely monitor the contents of their refrigerator and automatically order items when they fall below a certain threshold. The system utilizes Internet of Things (IoT) principles, Python programming language, Edge Impulse for machine learning model building, and the aiogram package for Telegram bot designing.

## Hardware / Software used
- **RaspberryPi**
- **Pi-Camera**
- **Raspbian OS**
- **Edge Impulse** : For Model Training (Machine Learning) (MobileNetSSD)
- **Python**
- **Aiogram Package** : For Telegram Bot Designing
## Features

- **Telegram Integration**: Users can interact with the smart refrigerator system through a Telegram bot, receiving real-time updates on refrigerator contents and placing orders.
  
- **Automatic Ordering**: When the quantity of an item in the refrigerator falls below a predefined threshold, the system automatically generates an order to restock the item.

- **Manual Stock Update**: Users can manually update the stock of items in the refrigerator by clicking a button in the Telegram bot interface.

- **Stock Image Capture**: With the integration of a Pi camera and Raspberry Pi, users can capture images of items in the refrigerator by clicking a button in the Telegram bot interface.

- **Order History**: Users can view their order history through the Telegram bot, allowing them to track their purchases over time.

- **Order Status**: The system provides real-time order status updates to users, informing them of the progress of their orders.

- **Change Threshold Value**: Users can adjust the threshold value for each item in the refrigerator through the Telegram bot interface, enabling customization of the restocking criteria.


## Screenshots

**Activity Diagram**

1. Counting Activity

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/8509f44a-2859-43ee-b035-91e4368a8b16" height="250">

2. Ordering Activity

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/9fce8a1b-3c39-4c91-bdf4-de915155091d" height="250">




**Telegram Bot UI**

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/de9e6331-38d8-45f1-8340-8bd6ceda0c20" height="250">
<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/b001753a-0a41-4f26-9603-d6d54d33849f" height="250">


**EDGE Impulse** : Model Training Dataset size:

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/08a4dbe5-2c31-4d5f-ab28-bcad5f67b015" height="250">

Accuracy :

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/a7e7c8a9-9a86-4158-9082-29ba23e80856" height="250">

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/186af8b3-2462-458a-8dad-200eaa1c2ca3" height="250">



**Model Sketch**

<img src="https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/dda535c6-4135-4c14-a675-45b87d4412a6" height="250">


**Real Life Model**

![real life smart fridge](https://github.com/DeepScripts/Smart-Telegram-Refrigerator/assets/125107549/8afd7129-b735-499d-9deb-4c138c4f4539)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/smart-refrigerator.git
   cd smart-refrigerator
