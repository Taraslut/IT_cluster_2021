import sys

from pprint import pprint

from lesson_19.connector_factory import (
    FactoryConnector,
    JsonConnector,
    XMLConnector,
    TXTConnector
)


def connect_factory(file_path: str):
    if file_path.endswith("json"):
        connector = JsonConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    elif file_path.endswith('txt'):
        connector = TXTConnector
    else:
        raise ValueError(f"There is no such connector fo file name {file_path}")
    return connector


def connect_to(file_path: str) -> FactoryConnector:
    factory = None
    try:
        factory = connect_factory(file_path)
    except Exception as e:
        print(e)
        raise e
    return factory(file_path)


if __name__ == "__main__":
    params = sys.argv
    if not len(params) == 2:
        print("usage: \n example_factory.py file_name\n")
        exit(1)

    file_name = params[1]
    data = connect_to(file_name)
    print("=" * 100)
    print(f"Person is {data.parsed_data['name']}")
    print("+" * 100)
    pprint(data.parsed_data)
