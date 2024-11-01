.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/ensuro.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/ensuro
    .. image:: https://readthedocs.org/projects/ensuro/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://ensuro.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/ensuro/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/ensuro
    .. image:: https://img.shields.io/pypi/v/ensuro.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/ensuro/
    .. image:: https://img.shields.io/conda/vn/conda-forge/ensuro.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/ensuro
    .. image:: https://pepy.tech/badge/ensuro/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/ensuro
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/ensuro

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

======
ensuro
======


    Prototype and wrappers to work with Ensuro Smart Contracts


This package is for working with the Ensuro Protocol (https://github.com/ensuro/ensuro) from Python.

It includes the prototype written in pure-python that can be used for simulation of Ensuro. Also includes
the wrappers that together with the compiled contracts can be used to deploy or use contracts deployed on the
blockchain.


Getting information from Ensuro objects
=======================================

 PremiumsAccount
  * ``.active_pure_premiums``
  * ``.surplus``: balance of pure premiums of finalized policies.
  * ``.won_pure_premiums``: accumulated pure premiums of expired/not defaulted policies.
  * ``.borrowed_active_pp``: pure premiums of active policies that were used for payouts. Always ``<= active_pure_premiums` and always = 0 if won_pure_premiums != 0``.
  * ``.pure_premiums``: it's a property that computes the total pure premiums as ``self.active_pure_premiums + self.won_pure_premiums - self.borrowed_active_pp``

EToken
  * ``.total_supply()``: total amount in dollars in the pool.
  * ``.scr``: amount that it's locked as solvency capital of active policies
  * ``.scr_interest_rate``: weighted average of the interest rate paid by the active policies
  * ``.utilization_rate``: percentage of utilization of the eToken. Property calculated as ``scr / total_supply``
  * ``.token_interest_rate``: interest rate for the EToken, it's calculated as ``scr_interest_rate * utilization_rate``
  * ``.funds_available``: available capital (total_supply - scr)
  * ``.funds_available_to_lock``: available capital that can be used as scr, ``(total_supply - scr) * max_utilization_rate``
  * ``.total_withdrawable()``: amount that can be withdrawn, considering the liquidity_requirement.
  * ``.get_loan()``: current debt of the pool with this eToken

RiskModule
  * ``.active_exposure``: total exposure currently allocated for this module
  * ``.get_minimum_premium(payout, loss_prob, expiration)``: minimum premium



Copying files from Ensuro main repository
=========================================

Instructions to copy files from ensuro repository::

    rm src/ensuro/contracts/*.json
    for x in `find ../ensuro/artifacts/contracts/ -maxdepth 2 -name "*.json" -not -name "*.dbg.json" `; do
        cp $x src/ensuro/contracts/ ;
    done
    for x in `find ../ensuro/artifacts/contracts/interfaces/ -maxdepth 2 -name "*.json" -not -name "*.dbg.json" `; do
        cp $x src/ensuro/contracts/ ;
    done
    for x in ERC1967Proxy.json IERC20Metadata.json IERC20.json IERC721.json ; do
        cp `find ../ensuro/artifacts/@openzeppelin/ -name $x` src/ensuro/contracts/$x ;
    done
    cp ../ensuro/artifacts/contracts/mocks/TestCurrency.sol/TestCurrency.json src/ensuro/contracts/TestCurrency.json
    cp ../ensuro/prototype/ensuro.py src/ensuro/prototype.py
    cp ../ensuro/prototype/wrappers.py src/ensuro/wrappers.py
    cp ../ensuro/prototype/utils.py src/ensuro/utils.py

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
