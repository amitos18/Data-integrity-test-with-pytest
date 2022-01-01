import pytest

from test_infra import TestInfra


class Test:
    infra = TestInfra()
    names_list = infra.generate_names_list()

    # Using pytest fixtures to pass random persons data to the test on each run
    @pytest.fixture
    def expected_persons_data(self):
        return self.infra.generate_persons_data_list(self.names_list)

    # The test compares the actual persons data list to the expected one
    @pytest.mark.parametrize("expected_persons_data", ["Data integrity test for APIS"], indirect=True)
    def test_data_integrity(self, expected_persons_data):
        actual_persons_data = self.infra.generate_persons_data_list(self.names_list)
        assert actual_persons_data == expected_persons_data
