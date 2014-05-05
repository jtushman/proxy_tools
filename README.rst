proxy_tools
==============

I'm just a proxy

|Build Status|

Loveingly extracted from `werkzeug`_.  A very useful proxy implementation, that I found to be useful outside
the web context -- hence the extraction.

Install
-------

.. code:: bash

    pip install proxy

.. |Build Status| image:: https://travis-ci.org/jtushman/proxy.svg?branch=master
   :target: https://travis-ci.org/jtushman/proxy_tools

Basic Usage
-----------

.. code:: python

    from proxy_tools import Proxy
    p = Proxy()

    def get_current_user():
        return User.find_by_id(request['user_id'])

    current_user = p(get_current_user)

    # Or alternatively

    from proxy_tools import module_property

    @module_property
    def current_user():
        return User.find_by_id(request['user_id'])

    # Then
    print(current_user.name)


Questions / Issues
------------------

Feel free to ping me on twitter: `@tushman`_
or add issues or PRs at https://github.com/jtushman/proxy_tools

.. _@tushman: http://twitter.com/tushman

Thank you
---------

To Armin Ronacher and the `werkzeug`_ team for their thought leadership and excellent work

.. _werkzeug: https://github.com/mitsuhiko/werkzeug

