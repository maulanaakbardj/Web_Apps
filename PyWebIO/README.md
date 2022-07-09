[PyWebIO](https://www.pyweb.io/)
==========

PyWebIO provides a diverse set of imperative functions to obtain user input and output content on the browser,
turning the browser into a "rich text terminal", and can be used to build simple web applications or browser-based
GUI applications. Using PyWebIO, developers can write applications just like writing terminal scripts
(interaction based on input and print function), without the need to have knowledge of HTML and JS.
PyWebIO is ideal for quickly building interactive applications that don't require a complicated user interface.

Features
------------

- Use synchronization instead of callback-based method to get input
- Non-declarative layout, simple and efficient
- Less intrusive: old script code can be transformed into a Web service only by modifying the input and output operation
- Support integration into existing web services, currently supports Flask, Django, Tornado, aiohttp and FastAPI(Starlette) framework
- Support for ``asyncio`` and coroutine
- Support data visualization with third-party libraries

Installation
--------------

Stable version::

    pip3 install -U pywebio

Development version::

    pip3 install -U https://code.aliyun.com/wang0618/pywebio/repository/archive.zip

