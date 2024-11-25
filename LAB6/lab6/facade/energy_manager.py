class EnergyManager:
    _instance = None

    @staticmethod
    def get_instance():
        if EnergyManager._instance is None:
            EnergyManager._instance = EnergyManager()
        return EnergyManager._instance

    def __init__(self):
        if EnergyManager._instance is not None:
            raise Exception("This is a Singleton class.")
        self.energy_usage = 0

    def monitor_usage(self):
        return self.energy_usage

    def optimize_energy(self):
        # Placeholder for optimization logic
        self.energy_usage = 50
