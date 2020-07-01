Python Tips
===========


:date: 2020-07-01 15:00
:modified: 2020-07-01 15:00
:slug: python-tips
:tags: python,tips,lists,functools,itertools,timezone
:lang: en



A collection of small Python scripts and tips.
..............................................

This post is based on a `Twitter thread`_ I started in April 2020 and works as a centralized way
to read all the tips in an easier format than Twitter's 280 characters.

Both will be updated frequently.

List Flatten without explicit loops
-----------------------------------

- Using Itertools' chain

.. code-block:: python


    import itertools

    test = [[-1, -2], [30, 40], [25, 35]]
    list(itertools.chain.from_iterable(test))

    >>  [-1, -2, 30, 40, 25, 35]


- Using **map** and strings (Suggested by `@Romestantc`_ )

.. code-block:: python

    test =  [[-1, -2], [30, 40], [25, 35]]
    map(int, ''.join(c for c in test.__str__() if c not in '[]').split(',') )

    >> [-1, -2, 30, 40, 25, 35]

Not pretty in my opinion ;)


Count  individual items of any iterable
---------------------------------------

.. code-block:: python

    from collections import Counter
    count = Counter(['a', 'b', 'c', 'a', 'a', 'b', 'd'])

    print(count)
    >> Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

    count['a']
    >> 3


Repeat a series of values from any iterable
-------------------------------------------

.. code-block:: python

    import itertools as it

    data = it.cycle([1, 2])

    for i in range(10):
        print(next(data))

    >> 1
    2
    1
    2
    1
    2
    1
    2
    1
    2


Name slices to reuse them
-------------------------

.. code-block:: python

    # slice(start, end, step)

    STEPTWO = slice(None, None, 2)
    integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    integer_list[STEPTWO]

    >> [0, 2, 4, 6, 8]


This is the same as:

.. code-block:: python

    integer_list[::2]


Reverse any "indexable" collection that supports slices
--------------------------------------------------------

.. code-block:: python

    # slice(None, None, -1) or [::-1]

    integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    integer_list[::-1]

    >> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


Use array to keep homogeneous type of objects in your lists
------------------------------------------------------------

.. code-block:: python

    from array import array

    integer_list = array('i', [1, 2, 3])

    integer_list = array('i', [1, 2, "a"])
    >> TypeError: an integer is required (got type str)

The constructor of array includes a type code parameter and an optional initial list.


Swap dictionary key-values using `zip`
---------------------------------------

Using **zip**:

.. code-block:: python

    data = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

    data.items()
    >> dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

    z = zip(data.values(), data.keys())

    dict(z)
    >>  { 1: 'a', 2: 'b', 3: 'c', 4: 'd' }


Using **dictionary comprehensions**:

.. code-block:: python

    data = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

    { v:k for k, v in data.items() }
    >>  { 1: 'a', 2: 'b', 3: 'c', 4: 'd' }


If there are repeated values, the result will be overwritten, so be careful.


Namedtuples as lightweight, inmutable, record-like objects
-----------------------------------------------------------

.. code-block:: python


    from collections import namedtuple

    Person = namedtuple("Person", "name age gender")
    bob = Person("Bob", 30, "male")

    bob.age
    >> 30

    bob[1]
    >> 30

Something similar can be achieved using Dataclasses (for Python 3.8+)



Built-ins set and frozenset for unordered collections of hashable objects
-------------------------------------------------------------------------

.. code-block:: python

    A = set([1, 2, 3])
    B = set([3, 4, 5])

    A.union(B)
    >> {1, 2, 3, 4, 5}

    A.intersection(B)
    >> {3}

    A.symmetric_difference(B)
    >> {1, 2, 4, 5}

**frozenset** has the same interface but returns an inmutable **set** object.


Itertools' dropwhile and takewhile to filter from an iterator
-------------------------------------------------------------

.. code-block:: python

    from itertools import  dropwhile

    numbers = [-2, -1, 0, 1, 2]

    f = lambda x: x < 1

    list ( dropwhile (f, numbers) )
    >>  [1, 2]


**takewhile**  takes the items if *True*. The difference with built-in function **filter**
is that the iteration stops whenever the test-function is false.

.. code-block:: python

    numbers = [-2, -1, 0, 1, 2, -3, -4]
    list(dropwhile(f, numbers))

    >> [1, 2, -3, -4]




As `@jgomo3`_ Observes, one way to think about those functions is that they simply divide a sequence in halves.

    takewhile gives you the first part.
    dropwhile the last part.



Traspose a matrix with List Comprehensions
------------------------------------------

.. code-block:: python

    M = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    MT = [[row[i] for row in M] for i in range(len(M))]

    print(MT)
    >> [[1, 4, 7], [2, 5, 8],  [3, 6, 9]]


Also, NumPy provides methods to for easier matrix manipulation.



Datetime to UTC
---------------

To create timezone aware datetimes in Python:

.. code-block:: python

    from datetime import datetime, timezone, timedelta

    tz = timezone(timedelta(hours=-6))  # UTC-6
    local = datetime(2020, 4, 16, 13, 40, 0, 0, tzinfo=tz)

    local.isoformat()
    >> '2020-04-16T13:40:00-06:00'


.. code-block:: python

    from datetime import datetime, timezone

    # assuming `local` is a datetime object

    print(local.isoformat() )
    >> '2020-04-16T13:40:00-06:00'

    local_in_utc = local.astimezone(timezone.utc)

    print(local_in_utc.isoformat())
    >> '2020-04-16T19:40:00+00:00'


You can always use **pytz** to handle timezones.

.. code-block:: python

    from datetime import datetime
    from pytz import timezone

    dt = datetime(2020, 4, 16, 13, 40, 0, tzinfo=pytz.utc)

    print(dt.isoformat())
    >> '2020-04-16T13:40:00+00:00'


functools.singledispatch  to achieve  parametric polymorphism in Python
-------------------------------------------------------------------------

.. code-block:: python

    from functools import singledispatch


    @singledispatch
    def process(num=None):
        raise NotImplementedError("Implement process function.")

    @process.register(int)
    def sub_process(num):
        # processing interger
        return f"Integer {num} has been processed successfully!"

    @process.register(float)
    def sub_process(num):
        # processing float
        return f"Float {num} has been processed successfully!"

    # use the function
    print(process(12.0))
    print(process(1))


.. _`Twitter thread`: https://twitter.com/jackboot7/status/1243321600507654144
.. _`@Romestantc`: https://twitter.com/Romestantc/status/1243655980203659265
.. _`@jgomo3` :  https://twitter.com/jgomo3/status/1248023890342920194
