from facade.lighting_system import LightingSystem
from facade.security_system import SecuritySystem
from facade.climate_control_system import ClimateControlSystem
from facade.entertainment_system import EntertainmentSystem
from facade.voice_control import VoiceControl

class SmartHomeFacade:
    def __init__(self):
        self.lighting_system = LightingSystem()
        self.security_system = SecuritySystem()
        self.climate_control_system = ClimateControlSystem()
        self.entertainment_system = EntertainmentSystem()
        self.voice_control = VoiceControl()

    def activateSecuritySystem(self):
        self.security_system.armSystem()

    def setClimateControl(self, targetTemp):
        self.climate_control_system.setTemperature(targetTemp)

    def controlLighting(self, action, level=None):
        if action == 'on':
            self.lighting_system.turnOnLights()
        elif action == 'off':
            self.lighting_system.turnOffLights()
        elif action == 'set_brightness':
            self.lighting_system.setBrightness(level)
