Ansible Stockclerk
==================

A  POC to validate Ansible inventory.

We generate a set of asserts based off the StockClerk model.  Ansible is
executed with a `--tags` flag, and the path to the playbook.  Ansible will
load all roles, thus having variables in scope, so that they can be asserted
for proper type.

This process is unable to identify undefined variables referenced throughout.

Usage
-----

    $ ansible-playbook -v -i inventory/az/az.ini --tags assert ~/git/ansible-systems/playbooks/openstack/metapod.yml

License
-------

MIT
