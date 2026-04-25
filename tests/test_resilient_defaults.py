import click


def test_callable_default_not_called_in_resilient_parsing():
    called = {"count": 0}

    def default():
        called["count"] += 1
        return "value"

    ctx = click.Context(click.Command("cmd"), resilient_parsing=True)
    option = click.Option(["--name"], default=default)

    result = option.get_default(ctx)

    assert called["count"] == 0
    assert callable(result)


def test_callable_default_called_in_normal_parsing():
    called = {"count": 0}

    def default():
        called["count"] += 1
        return "value"

    ctx = click.Context(click.Command("cmd"))
    option = click.Option(["--name"], default=default)

    result = option.get_default(ctx)

    assert called["count"] == 1
    assert result == "value"


def test_non_callable_default_unchanged():
    ctx = click.Context(click.Command("cmd"))
    option = click.Option(["--name"], default="hello")

    result = option.get_default(ctx)

    assert result == "hello"
