from AdminPanel import AdminPanel





if __name__ == '__main__':
    a1 = AdminPanel()

    a1.create_group('living_room')
    a1.create_multiple_devices('living_room', 'lamps', 5)

    a1.turn_on_all_in_group('living_room')
    a1.auto_control_lights()
    #a1.turn_off_all_in_group('living_room')
    # check koni bbini roshan

    #mygroups = a1.groups['living_room']

    # mygroups[1].name #lamps2'

    # mygroups[1].turn_on()

# besazi
