import PuzzleGame
from tkinter import *
import paho.mqtt.client as mqtt
import time


# Callback Function on Connection with MQTT Server
def on_connect(client, userdata, flags, rc):
    print("Connected with Code :" + str(rc))
    # Subscribe Topic from here
    client.subscribe("devices/11:22:33:55/inbox/User1/function/1")
    client.subscribe("devices/11:22:33:55/inbox/User1/function/2")
    client.subscribe("devices/11:22:33:55/inbox/User1/function/3")
    client.subscribe("devices/11:22:33:55/inbox/User1/function/4")


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(client, userdata, msg):
    # print the message received from the subscribed topic
    #message = msg.payload
    #message = message.decode()  # default decoding utf-8
    print(str(msg.payload))


def main():
    """
    main function, which create a tkinter object, and start the mqtt client
    and start the game
    """

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # client.connect("192.168.1.32", 4269, 60)
    # client.username_pw_set("11:22:33:55", "123")

    client.loop_start()
    # time.sleep(1)
    # while True:
        # client.publish("Tutorial", "Getting Started with MQTT")
        # print("Message Sent")
        # time.sleep(15)
    root = Tk()
    PuzzleGame.PuzzleGame(root, client)
    root.mainloop()
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    main()
