class RemoteController:
    def turn_on(self, appliance):
        appliance.start()

    def turn_off(self, appliance):
        appliance.stop()
