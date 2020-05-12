class ProgrammingLanguage:
    def __init__(self, lang_name, typing, reflection, year):
        """Constructor method"""
        self.lang_name = lang_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".\
            format(self.lang_name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Dynamic type."""
        return self.typing == "Dynamic"


def test():
    """Run simple tests/demos on ProgrammingLanguage class."""
    java = ProgrammingLanguage('Java', 'Static', 'Yes', 1995)
    c_plus_plus = ProgrammingLanguage('C++', 'Static', 'No', 1983)
    python = ProgrammingLanguage("Python", "Dynamic", 'Yes', 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", 'No', 1991)
    ruby = ProgrammingLanguage('Ruby', 'Dynamic', 'No', 1995)

    languages = [java, c_plus_plus, python, visual_basic, ruby]
    print(python)

    print("The typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.lang_name)


if __name__ == "__main__":
    test()