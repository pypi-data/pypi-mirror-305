=======
History
=======

2.1.0 (October 30th, 2024)
==========================

Changes:

* Transfer repository from willkg to mozilla-services.
* Drop support for Python 3.8. (#158)
* Add support for Python 3.13. (#152)
* Support ``_return_query`` in supersearch and supersearchfacet. (#140)
* Fix start-date and end-date handling in supersearchfacet. (#136)
* Handle non-JSON error responses correctly. (#139)
* Add download stats and estimate to fetch-data. (#149)
* Add documentation for default data window in supersearch docs. (#147)
* Support ``.env`` files for ``CRASHSTATS_API_TOKEN`` for all commands. (#154)


2.0.0 (April 12th, 2024)
========================

Changes:

* Radically improve README documentation.
* Add estimates to reprocess command. (#80)
* Add support for "csv" format for supersearch and supersearchfacet. (#88)
* Drop support for Python 3.7. (#90)
* Add support for Python 3.12. (#91)
* Add "raw" format for better debugging.
* Add ``_histogram`` support. (#98)
* Add ``--denote-weekends`` to supersearchfacet. (#54)
* Implement parallelization for fetch-data. (#106)
* Implement ``--leftover-count`` and ``--no-leftover-count`` for supersearchfacet. (#109)
* Fix user-agent to reflect crashstats-tools version. (#121)
* Add support for nested aggs and cardinality. (#102, #103)
* Move functions for Crash Stats API to libcrashstats library. (#67)


1.4.0 (November 18th, 2022)
===========================

Changes:

* Fix supersearch to kick up a usage error when you use columns that don't
  exist or that you don't have access to. (#61)
* Fix supersearchfacet to kick up a usage error when you use columsn that don't
  exist or that you don't have access to. (#62)
* Fix fetch-data to use Socorro crashstorage layout. (#66)
* Fix fetch-data to work with new raw crash structure.
* Remove pkg_resources use. (#70)
* Add markdown output to supersearch. (#52)
* Rework output for supersearch and supersearchfacet so that format=tab can
  stream results. This is helpful for incremental progress and when using it
  with pipes. (#39)
* Add support for Python 3.11 (#63)
* Add ``--overwrite/--no-overwrite`` to fetch-data so it does less work. (#58)
* Add support for ``--period=weekly`` to supersearchfacet. (#24)
* Add tests for supersearchfacet. (#50)
* Add tests for supersearch. (#16)
* Add tests for reprocess. (#14)
* Add tests for fetch-data. (#15)


1.3.0 (June 28th, 2022)
=======================

Changes:

* Improve output using rich. (#47)
* Add ``--allow-many`` argument to reprocess.
* Fix non-string sorting.
* Add "remainder" column in supersearchfacet.


1.2.0 (October 26th, 2021)
==========================

Changes:

* Add support for Python 3.9. (#30)
* Add support for Python 3.10. (#40)
* Drop support for Python 3.6.
* Switch to ``src/`` layout (#31)
* Rework supersearchfacet periods in supersearchfacet command so it support
  other periods like "hourly".
* Add support for specifying pipeline with reprocess command.
* Improve crash id argument handling to error out better.


1.1.1 (June 29th, 2020)
=======================

Bugs:

* Fix ``--num=all`` in supersearch. (26)


1.1.0 (May 21, 2020)
====================

Features:

* Rewrite commands to use click instead of argparse for argument parsing. (#17)
* Add ``supersearchfacet`` command. (#2)


1.0.4 (January 7, 2020)
=======================

Features:

* Add support for CRASHID, bp-CRASHID, and
  https://crash-stats.mozilla.org/report/index/CRASHID formats of crash id in
  reprocess and fetch_data commands.
* Add tests for utils functions. (#1)


1.0.3 (October 23rd, 2019)
==========================

Bugs:

* Handle HTTP 400 errors better so the user sees the error message
  in the HTTP response.
* Change examples to use single-quote which won't expand things in
  the shell.
* Redo the prompt when reprocessing > 10,000 crash reports.
* Fix the aggregation argument check.
* Remove IRC channel references--we don't use IRC anymore.


1.0.2 (August 22nd, 2019)
=========================

Features:

* Add ``reprocess`` command. (#4)


1.0.1 (July 31st, 2019)
=======================

Bugs:

* Fix saving ``dump_names``.


1.0.0 (July 31st, 2019)
=======================

* Initial writing with ``supersearch`` and ``fetch-data`` commands.
