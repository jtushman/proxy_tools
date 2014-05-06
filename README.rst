proxy_tools
==============

Did you every want to have @property on a module? ...

|Build Status|

Loveingly extracted from `werkzeug`_.  A very useful proxy implementation, that I found to be useful outside
the web context -- hence the extraction.

Impetus
-------

I was working on a module and I wanted it to have a @property like you can do on `objects`.  No dice.  
I found an elegant implementation within werkzeug with request and session and the like.  So I extracted it so we can use it
for our non-werkzeug projects.

For more on the nitty gritty on why this works, checkout this `post`_ 

.. _post: http://jtushman.github.io/blog/2014/05/02/module-properties/

Install
-------

.. code:: bash

    pip install proxy_tools

.. |Build Status| image:: https://travis-ci.org/jtushman/proxy_tools.svg?branch=master
   :target: https://travis-ci.org/jtushman/proxy_tools

Basic Usage
-----------

.. code:: python

    # your_module/__init__.py
    from proxy_tools import module_property

    @module_property
    def current_user():
        return User.find_by_id(request['user_id'])
        
    # Then elsewhere
    from your_module import current_user
    print(current_user.name)


Alternative Syntax

.. code:: python

    from proxy_tools import Proxy

    def get_current_user():
        return User.find_by_id(request['user_id'])

    current_user = Proxy(get_current_user)


Questions / Issues
------------------

Feel free to ping me on twitter: `@tushman`_
or add issues or PRs at https://github.com/jtushman/proxy_tools

.. _@tushman: http://twitter.com/tushman

Thank you
---------

To Armin Ronacher and the `werkzeug`_ team for their thought leadership and excellent work

.. _werkzeug: https://github.com/mitsuhiko/werkzeug

