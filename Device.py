import time
import random

class Sensor:
    def __init__(self, topic, pin=100):
        self.topic = topic
        self.topic_list = self.topic.split('/')

        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.pin = pin  # sensor pin

    def read_sensor(self):

        if self.device_type == 'thermo':

            a = np.random.uniform(22, 27)
            self.curren_value = a
            return self.curren_value

        elif self.device_type == 'light':

            a = np.random.uniform(0, 100)
            self.curren_value = a
            return self.curren_value



class Device:
    def __init__(self, topic, mqtt_broker='localhost', port=1883):

        self.topic = topic

        self.topic_list = self.topic.split('/')
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.port = port
        self.mqtt_broker = mqtt_broker
        self.status = 'off'
        self.speed = 0

        # self.connect_mqtt()
        # self.setup_gpio()

    def connect_mqtt(self):

        self.mqtt_client.connect(self.mqtt_broker, self.port)
        print(f'{self.name} connected to mqtt')

    def setup_gpio(self):
        if self.device_tye == 'lights':
            GPIO.setup(17, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'doors':
            GPIO.setup(27, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'fans':
            GPIO.setup(22, GPIO.OUT)
            if self.speed > 0:
                GPIO.setup(18, GPIO.OUT)  # For fan speed, if using PWM
                # self.pwm = GPIO.PWM(18, 100)  # PWM frequency 100Hz
                # self.pwm.start(0)
                print(f'{self.name} connected to gpio')

    def turn_on(self):
        self.status = 'on'
        print(f'{self.name} is turned on')
        # self.send_command('TURN_ON') #ramzie k toye MQTT
        if self.device_type == 'lights':
            pass
            # GPIO.output(17, GPIO.HIGH)

        elif self.device_type == 'doors':
            pass
            # GPIO.output(27, GPIO.HIGH)

        elif self.device_type == 'fans':
            pass
            # GPIO.output(22, GPIO.HIGH)

    def set_speed(self, speed):

        if self.status == 'off':
            print(f'{self.name} currently is off')
            return None

        else:
            self.speed = speed
            # self.send_command(f'SET_SPEED:{speed}')

    def turn_off(self):
        self.status = 'off'
        print(f'{self.name} is turned off')
        # self.send_command('TURN_OFF')
        if self.device_type == 'lights':
            # GPIO.output(17, GPIO.LOW)
            pass

        elif self.device_type == 'doors':
            # GPIO.output(27, GPIO.LOW)
            pass

        elif self.device_type == 'fans':
            # GPIO.output(22, GPIO.LOW)
            pass

    def get_status(self):
        return self.status

    def send_command(self, command):
        '''send a command via MQTT'''
        self.mqtt_client.publish(self.topic, command)
        print(f'command {command} send to topic {self.topic}')