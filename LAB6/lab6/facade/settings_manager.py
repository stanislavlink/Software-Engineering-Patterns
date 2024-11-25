class SettingsManager:
    _instance = None

    @staticmethod
    def get_instance():
        if SettingsManager._instance is None:
            SettingsManager._instance = SettingsManager()
        return SettingsManager._instance

    def __init__(self):
        if SettingsManager._instance is not None:
            raise Exception("This is a Singleton class.")
        self.preferred_temperature = 72  # Default temperature
        self.lighting_preset = "Soft"

    def update_temperature(self, temp):
        self.preferred_temperature = temp
