import click


def test_default_callback_not_called_in_resilient_parsing():
    called = {"count": 0}

    def default():
        called["count"] += 1
        return "value"

    ctx = click.Context(click.Command("cmd"), resilient_parsing=True)

    option = click.Option(["--name"], default=default)

    option.get_default(ctx)

    assert called["count"] == 0
