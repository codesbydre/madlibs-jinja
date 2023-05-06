"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["animal", "verb", "adverb", "food"],
    """A {animal} was walking through the woods when it started to {verb} {adverb}. It eventually found some {food} to eat."""
)

story3 = Story(
    ["food", "proper_noun", "place", "animal"],
    """
    It was {food} day at school, and {proper_noun} went to {place} to eat. However, a {animal} stole {proper_noun}'s lunch.
    """
)

stories = {'Story1': story1,
           'Story2': story2,
           'Story3': story3}
