def assert_status_code(operation, expected_code, actual_code):
    if expected_code != actual_code:
        assert False, "Expected operation \"{}\" to return status code {}, instead got status code {}"\
            .format(operation, expected_code, actual_code)


def assert_data(field, expected_data, actual_data):
    if expected_data != actual_data:
        assert False, "Expected data for \"{}\" to be {}, instead got {}"\
            .format(field, expected_data, actual_data)
