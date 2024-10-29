CSVtoTable
==========
Simple command-line utility to convert CSV files to searchable and
sortable HTML table. Supports large datasets and horizontal scrolling for large number of columns.

DISCLAIMER:
----
This is NOT an official version, nor am I affiliated with the original creator Vivek R @vividvilla https://github.com/vividvilla (Upstream Author)
This version is mostly for me, if you wanna use it too go ahead but I give no promises of function.
if you notice any errors or issues please tell me!

Demo
----

`Here is a demo`_ of `sample csv`_ file converted to HTML table.

.. image:: https://raw.githubusercontent.com/NanashiTheNameless/csvtotable/master/sample/table.gif

Installation
------------

::

    python -m pip install --upgrade 'csvtotable @ git+https://github.com/NanashiTheNameless/csvtotable@master'


Get started
-----------

::

    csvtotable --help

Convert ``data.csv`` file to ``data.html`` file

::

    csvtotable data.csv data.html

Open output file in a web browser instead of writing to a file

::

    csvtotable data.csv --serve

Options
-------

::

    -c,  --caption          Table caption and HTML title
    -t,  --title            Alias of Caption
    -d,  --delimiter        CSV delimiter. Defaults to ','
    -q,  --quotechar        Quote chracter. Defaults to '"'
    -dl, --display-length   Number of rows to show by default. Defaults to -1 (show all rows)
    -o,  --overwrite        Overwrite the output file if exists. Defaults to false.
    -s,  --serve            Open html output in a web browser.
    -h,  --height           Table height in px or in %. Default is 75% of the page.
    -p,  --pagination       Enable/disable pagination. Enabled by default.
    -vs, --virtual-scroll   Number of rows after which virtual scroll is enabled. Default is set to 1000 rows.
                            Set it to -1 to disable and 0 to always enable.
    -nh, --no-header        Show default headers instead of picking first row as header. Disabled by default.
    -e,  --export           Enable filtered rows export options.
    -eo, --export-options   Enable specific export options. By default shows all.
                            For multiple options use -eo flag multiple times. For ex. -eo json -eo csv

Credits
-------
`Datatables`_

.. _Here is a demo: https://cdn.rawgit.com/NanashiTheNameless/csvtotable/2.1.0/sample/goog.html
.. _sample csv: https://github.com/NanashiTheNameless/csvtotable/blob/master/sample/goog.csv
.. _Datatables: https://datatables.net
