import click


def test_choice_returns_canonical_value():
    choice = click.Choice(["RED"], case_sensitive=False)

    result = choice.convert("red", None, None)

    assert result == "RED"
