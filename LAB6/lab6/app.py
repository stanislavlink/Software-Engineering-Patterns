from facade.smart_home_facade import SmartHomeFacade
from facade.settings_manager import SettingsManager
from facade.energy_manager import EnergyManager
from bridge.remote_controller import RemoteController
from bridge.appliances import Appliances

# Test the Facade
smart_home = SmartHomeFacade()
smart_home.activateSecuritySystem()
smart_home.setClimateControl(72)
smart_home.controlLighting("on")

# Singleton Usage
settings = SettingsManager.get_instance()
settings.update_temperature(74)
print(f"Preferred Temperature: {settings.preferred_temperature}")

energy_manager = EnergyManager.get_instance()
energy_manager.optimize_energy()

# Test the Bridge Pattern
appliance = Appliances()
remote = RemoteController()
remote.turn_on(appliance)
remote.turn_off(appliance)
