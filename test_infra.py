from apis_handler import AgeApi, GenderApi, NationalitiesApi
from person_data import PersonData
import names


# An interface for preforming api calls and building the results objects (expected and actual results)

class TestInfra:
    # Used for building both expected and actual persons data
    # Creates a list of person PersonData objects
    def generate_persons_data_list(self, names_list):
        age_api = AgeApi()
        gender_api = GenderApi()
        nationalities_api = NationalitiesApi()
        persons_data_list = []

        for user_name in names_list:
            user_age = age_api.extract_relevant_data(user_name)
            user_gender = gender_api.extract_relevant_data(user_name)
            user_nationality = nationalities_api.extract_relevant_data(user_name)
            user_obj = PersonData(user_name, user_age, user_gender, user_nationality)
            persons_data_list.append(user_obj)

        return persons_data_list

    def generate_names_list(self):
        return [names.get_first_name() for i in range(5)]
