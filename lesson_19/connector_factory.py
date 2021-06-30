import json


class FactoryConnector:

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def parsed_data(self):
        raise NotImplemented("The method is not released.")


class JsonConnector(FactoryConnector):

    def __init__(self, file_name):
        super(JsonConnector, self).__init__(file_name)
        # self.data =json.loads("some_json_string")
        with open(self.file_name) as file:
            self.data = json.load(file)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(FactoryConnector):
    def __init__(self, file_name):
        super(XMLConnector, self).__init__(file_name)
        with open(self.file_name) as file:
            self.data = xml.parsers(file)

    @property
    def parsed_data(self):
        return self.data


class TXTConnector(FactoryConnector):
    pass