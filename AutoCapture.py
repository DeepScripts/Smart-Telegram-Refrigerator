import asyncio
from picamera2 import Picamera2, Preview
import datetime
from module import ObjectDetection as obj
from module.order import send_message
import json

empty={}
order={}
get_order = {}

##Threshhold Limit
limit = {}

def check_anyOrder():
    with open("order.txt", "r") as file:
        lines = file.readlines()
    num_lines = len(lines)
    return num_lines
    

def count_item():
    count={}
    with open('threshold.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        key, value = line.strip().split(' : ')
        limit[key] = int(value)
    print("Current Threshold Limit : ",limit)

    count = obj.classify("./image/autoimage.jpg")
    with open("./count.txt", "w") as f:
        for key, value in count.items():
            f.write(key + " : " + str(value) + "\n")
    print(f"Current Stock: {count}")
    for key in limit:
        if limit[key] > count[key]:
            order[key]= limit[key] - count[key]
    if order is not None and bool(order):
        print(f"Order to be placed: {order}")
    return order

async def capture_image():
    try:
        picam2 = Picamera2()
        camera_config = picam2.create_still_configuration(main={"size": (1280, 720)}, lores={"size": (640, 480)}, display="lores")
        picam2.configure(camera_config)
        while True:
            await asyncio.sleep(2)  # give the camera time to warm up
            picam2.start()
            print("Starting Camera...")
            filename = './image/autoimage.jpg'
            picam2.capture_file(filename)
            print(f'Image captured: {filename}')
            current_time = datetime.datetime.now()
            time_str = current_time.strftime("%I:%M %p %d-%m-%Y")
            print(time_str)
            with open('./time.txt', 'w') as f:
                f.write(time_str)
            print("Camera Stop.\nWaiting for Classification")
            picam2.stop()
            get_order = count_item()
            if check_anyOrder() == 0 :
                await send_message(get_order)
                try:
                    get_order["Status"] = "Pending"
                    get_order["Order_Date"] = f"{datetime.datetime.now().strftime('%I:%M %p %d-%m-%Y')}"
                    with open("./order.txt", "w") as f:
                        for key, value in get_order.items():
                            f.write(key + " : " + str(value) + "\n")
                except:
                    print("Order File Cannot Write !!")
            else:
                print("One Order Pending")
            order=empty
            get_order=empty
            await asyncio.sleep(30) # wait for 30 seconds before capturing the next image
    except:
        print("Someting Wents wrong with Camera Try again")

async def main():
    await capture_image()

if __name__ == '__main__':
    asyncio.run(main())




