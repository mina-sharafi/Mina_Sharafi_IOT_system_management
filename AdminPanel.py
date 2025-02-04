from Device import Device
from Device import Sensor
from datetime import datetime


class AdminPanel:

    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        ''' give me the name for one section of your house'''

        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'groups {group_name} created')
            # logg mimone
        else:
            print('yout group name is duplicated name')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)



        else:
            print(f'Group {group_name} does not exist')

    # dota function ro neveshtam ta inja bvrsm

    def create_device(self, group_name, device_type, name):

        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            # task2
            print(f'Device "{name}" created and added to group "{group_name}".')

        else:
            print(f'Group {group_name} does not exist')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f"{device_type}{i}"

                topic = f'home/{group_name}/{device_type}/{device_name.lower()}'

                new_device = Device(topic)

                self.add_device_to_group(group_name, new_device)
            # task_2
            print(f'{number_of_devices} added to group "{group_name}".')

        else:
            print(f'Group {group_name} does not exist')

    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]

        else:
            print(f'Group {group_name} does not exist')
            return []

    def turn_on_all_in_group(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_on()
        print(f'Turn in on all device in {group_name}.')

    def turn_off_all_in_group(self, group_name):
        # task_2
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_off()
        print(f'Turn in off all device in {group_name}.')

        ''' hameye cheragh haye yek goroh ra khamosh konad'''

    def trun_on_all(self):
        # task_2
        for group_name in self.groups:
            self.turn_on_all_in_group(group_name)
        print("Turning ON all devices in all groups")

    def turn_off_all(self):
        for group_name in self.groups:
            self.turn_off_all_in_group(group_name)
        print("Turning OFF all devices in all groups")
        '''hameye devcie haro khamosh kone'''

    def get_status_in_group(self, group_name):
        # task_2
        if group_name in self.groups:
            for device in self.groups[group_name]:
                print(f' status of devices in group "{group_name}" : {device.topic}: {device.status}')
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''

    def get_status_in_device_type(self, device_type):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    print(f'{device.name}: {device.status}')
                else:
                    print(f'No devices of type {device_type} found.')
        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''

    def create_sensor(self):
        # bar asase clASS SENSOR argument bzarid
        pass

    def get_status_sensor_in_group(self, group_name):

        '''

        sensor haye yek goroh ro biad doone dooen status ro pas bde

        '''
        pass
# task_3
    def auto_control_lights(self):
        #baraye tosee ayandeh mishe fasl ra ham be in ezafeh kard ke dar nime aval sal dirtar roshan shavad
        #va dar nime dovom sal be khater zoodtar tarik shodan hava lamp ha zodtar roshan shavad
        #mishavad ba tavajoh be mogheyat goghrafiyayi noor ra control kard
        current_hour = datetime.now().hour
        for group_name in self.groups:
            for device in self.groups[group_name]:
                if device.device_type == 'lamps':
                    if 18 <= current_hour <= 22:
                        device.turn_on()
                        print("Evening vibes! Lights ON from 6 PM to 10 PM 🌙✨")
                    else:
                        device.turn_off()
                        print("Saving energy! Lights OFF 🌞")

