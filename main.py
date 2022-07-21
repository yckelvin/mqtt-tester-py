def on_button_pressed_a():
    microIoT.microIoT_SendMessage(convert_to_text(pins.analog_read_pin(AnalogPin.P0)),
        microIoT.TOPIC.TOPIC_0)
    microIoT.microIoT_initDisplay()
    microIoT.microIoT_showUserText(0,
        "Light value:" + convert_to_text(pins.analog_read_pin(AnalogPin.P0)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def publish(num: number, text: str):
    microIoT.microIoT_SendMessage(text, microIoT.TOPIC.TOPIC_0)
    microIoT.microIoT_showUserText(num, "Send... " + text)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

wifi_name = "izowifi"
password = "izo1234@"
iot_id = "lmZB9bXGR"
iot_pwd = "liWfrxXMgz"
topic_0 = "qwPmNL37g"
microIoT.microIoT_initDisplay()
microIoT.microIoT_showUserText(0, "INIT DEVICE")
microIoT.microIoT_showUserText(1, "SETUP WIFI")
microIoT.microIoT_WIFI(wifi_name, password)
microIoT.microIoT_showUserText(2, "DEFINE MQTT")
microIoT.microIoT_MQTT(iot_id, iot_pwd, topic_0, microIoT.SERVERS.ENGLISH)
publish(4, convert_to_text(randint(0, 20)))
publish(5, convert_to_text(randint(0, 20)))
publish(6, convert_to_text(randint(0, 20)))