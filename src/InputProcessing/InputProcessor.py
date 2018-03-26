def input_processor(message, validator=lambda value: value, parser=lambda value: value,
                    pre_parse_validator=lambda value: True):
    while True:
        choice_raw = input(message)

        try:
            if pre_parse_validator(choice_raw):
                choice_parsed = parser(choice_raw)

                if validator(choice_parsed):
                    return choice_parsed

        except ValueError:
            pass

        print("Invalid input. Please try again.\n")