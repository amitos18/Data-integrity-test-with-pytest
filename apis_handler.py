from abc import ABC, abstractmethod
import requests


# An abstract class for handling multiple APIs

class ApisHandler(ABC):

    @abstractmethod
    def extract_relevant_data(self):
        pass

    # Error handling in case of unwanted failures on the API (tested)
    def data_not_found_exception(self, key):
        raise Exception(f"your key {key} does not found in the API")

    def call_api(self, name):
        path = self.create_api_path(name)
        return requests.get(path).json()

    @abstractmethod
    def create_api_path(self):
        pass


class AgeApi(ApisHandler):

    def extract_relevant_data(self, name):
        json_data = self.call_api(name)
        key_to_find = "age"

        for key in json_data:
            if key == key_to_find:
                return json_data[key]

        return self.data_not_found_exception(key_to_find)

    def create_api_path(self, name):
        return f"https://api.agify.io?name={name}"


class GenderApi(ApisHandler):

    def extract_relevant_data(self, name):
        json_data = self.call_api(name)
        key_to_find = "gender"

        for key in json_data:
            if key == key_to_find:
                return json_data[key]

        return self.data_not_found_exception(key_to_find)

    def create_api_path(self, name):
        return f"https://api.genderize.io?name={name}"


class NationalitiesApi(ApisHandler):

    # This method finds the country id with the highest probability, which is always the first one.
    def extract_relevant_data(self, name):
        json_data = self.call_api(name)
        key_to_find = "country"
        sub_key_to_find = "country_id"

        for key in json_data:
            if key == key_to_find:
                countries_json_obj = json_data[key][0]
                for sub_key in countries_json_obj:
                    if sub_key == sub_key_to_find:
                        return countries_json_obj[sub_key]

        return self.data_not_found_exception(key_to_find)

    def create_api_path(self, name):
        return f"https://api.nationalize.io?name={name}"
