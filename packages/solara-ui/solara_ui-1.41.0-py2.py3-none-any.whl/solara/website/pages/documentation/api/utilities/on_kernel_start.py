"""
# on_kernel_start

Run a function when a virtual kernel (re)starts and optionally run a cleanup function on shutdown.

```python
def on_kernel_start(f: Callable[[], Optional[Callable[[], None]]]) -> Callable[[], None]:
    ...
```

`f` will be called on each virtual kernel (re)start. This (usually) happens each time a browser tab connects to the server
[see solara server for more details](https://solara.dev/docs/understanding/solara-server).
The (optional) function returned by `f` will be called on kernel shutdown.

Note that the cleanup functions are called in reverse order with respect to the order in which they were registered
(e.g. the cleanup function of the last call to `on_kernel_start` will be called first on kernel shutdown).

The return value of on_kernel_start is a cleanup function that will remove the callback from the list of callbacks to be called on kernel start.

During hot reload, the callbacks that are added from scripts or modules that will be reloaded will be removed before the app is loaded
again. This can cause the order of the callbacks to be different than at first run.
"""

from solara.website.components import NoPage

title = "on_kernel_start"
Page = NoPage
