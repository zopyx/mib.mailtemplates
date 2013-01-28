mib.datadog
===========

Pyramid integration with DataDog API

Configuration
-------------

You need to put the following options into the [app:XXX] section of
your Pyramid application::

    dog.enabled = True|False
    dog.api_key = <DataDog API key, see web UI>
    dog.application_key = <DataDog application key, see web UI>

Usage
-----

Send simple DataDog events
++++++++++++++++++++++++++

The notify() method encapsulates the ``dogapi.event()`` API 
by dealing with the HTTP authentication for you::


    from mib.datadog import notify
    notify('Application started, priority='low')     

Request logging through a Pyramid tween
+++++++++++++++++++++++++++++++++++++++

The ``mib.datadog`` module provides a simple request monitoring functionality
for logging the number of requests and the request-response time to DataDog.
The functionality is implemented as a Pyramid tween and can easily be
enabled by adding the following line to the Pyramid configuration of your
package::

    config.add_tween('mib.datadog.tweens.timing_tween_factory')

The logging is automatically enabled if ``dog.enabled = True`` is set.


(Error) logging to DataDog
++++++++++++++++++++++++++

The module provides a standard Python ``logging`` handler that will send
logging messages (basically used for recording Python errors and their
traceback through DataDog(Error) logging to DataDog. Your Pyramid application
must contain a logger configuration similar to the following::


    [loggers]
    keys = root, mibpyramid

    [handlers]
    keys = console, dogapi

    [logger_root]
    level = INFO
    handlers = console, dogapi

    [logger_mibpyramid]
    level = INFO
    handlers = dogapi
    qualname = mib

    [handler_dogapi]
    class = mib.datadog.logger.DogAPILoggingHandler
    args = ()
    level = WARN
    formatter = generic

    ....

