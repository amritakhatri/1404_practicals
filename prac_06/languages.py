"""Client code to test the ProgrammingLanguage class.
Estimated time: 1 hour
Start time: 19:40
End time:
"""

from programming_language import ProgrammingLanguage

def main():
    """Create and display information about programming languages."""
    # Create programming language instances
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test __str__ method by printing instances
    print(python)
    print(ruby)
    print(visual_basic)

    # Store languages in a list
    languages = [python, ruby, visual_basic]

    # Find and display dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
