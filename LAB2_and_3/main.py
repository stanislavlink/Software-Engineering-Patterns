import json
from port import Port
from ship import Ship
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer


def load_data(file_path):
    """Завантаження даних з JSON-файлу."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_output(output_data, file_path='output.json'):
    """Збереження результатів у файл."""
    with open(file_path, 'w') as file:
        json.dump(output_data, file, indent=4)


def main():
    data = load_data('input.json')

    # Створення портів, кораблів і контейнерів
    ports = {}
    ships = {}
    containers = {}

    for item in data['ports']:
        port = Port(item['id'], item['latitude'], item['longitude'])
        ports[item['id']] = port

    for item in data['ships']:
        port = ports[item['port_id']]
        ship = Ship(item['id'], item['fuel'], port, item['max_weight'], item['max_containers'], item['fuel_per_km'])
        port.incoming_ship(ship)
        ships[item['id']] = ship

    for item in data['containers']:
        if item['type'] == 'basic':
            container = BasicContainer(item['id'], item['weight'])
        elif item['type'] == 'heavy':
            container = HeavyContainer(item['id'], item['weight'])
        elif item['type'] == 'refrigerated':
            container = RefrigeratedContainer(item['id'], item['weight'])
        elif item['type'] == 'liquid':
            container = LiquidContainer(item['id'], item['weight'])
        containers[item['id']] = container

    # Формування вихідного JSON
    output = {}
    for port_id, port in ports.items():
        port_data = {
            "lat": round(port.latitude, 2),
            "lon": round(port.longitude, 2),
            "basic_container": [c.id for c in port.containers if isinstance(c, BasicContainer)],
            "heavy_container": [c.id for c in port.containers if isinstance(c, HeavyContainer) and not isinstance(c, (
            RefrigeratedContainer, LiquidContainer))],
            "refrigerated_container": [c.id for c in port.containers if isinstance(c, RefrigeratedContainer)],
            "liquid_container": [c.id for c in port.containers if isinstance(c, LiquidContainer)],
            "ships": {}
        }
        for ship in port.current_ships:
            ship_data = {
                "fuel_left": round(ship.fuel, 2),
                "basic_container": [c.id for c in ship.containers if isinstance(c, BasicContainer)],
                "heavy_container": [c.id for c in ship.containers if isinstance(c, HeavyContainer) and not isinstance(c,
                                                                                                                      (
                                                                                                                      RefrigeratedContainer,
                                                                                                                      LiquidContainer))],
                "refrigerated_container": [c.id for c in ship.containers if isinstance(c, RefrigeratedContainer)],
                "liquid_container": [c.id for c in ship.containers if isinstance(c, LiquidContainer)]
            }
            port_data["ships"][f"ship_{ship.id}"] = ship_data

        output[f"port_{port_id}"] = port_data

    # Збереження результатів
    save_output(output)
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
