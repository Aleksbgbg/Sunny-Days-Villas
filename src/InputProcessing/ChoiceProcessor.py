def choice_processor(message, options, descriptions, parser):
    class Choice:
        def __init__(self, parsed, description, raw):
            self.parsed = parsed
            self.description = description
            self.raw = raw

        def __str__(self):
            return self.description

    message_options = "\n".join(f"({option}) {descriptions[index]}" for index, option in enumerate(options))

    message_prompt = f"{message}\n{message_options}\n"

    while True:
        choice_raw = input(message_prompt)

        try:
            choice_parsed = parser(choice_raw)

            if choice_parsed in options:
                return Choice(choice_parsed, descriptions[options.index(choice_parsed)], choice_raw)

        except ValueError:
            pass

        print("Invalid input. Please try again.\n")