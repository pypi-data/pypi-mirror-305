"""Utility apps, slightly more complex."""

import solara

redirect = None


@solara.component
def Page():
    return solara.Markdown("Should not see me")
