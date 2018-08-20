[![Build Status](https://travis-ci.org/novomatic-tech/ansible-role-common-pkg.svg?branch=master)](https://travis-ci.org/novomatic-tech/ansible-role-storage-init) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)

Ansible-role-common-pkg
=========

Install all common and extra packages that are not included in the corporation baseline template.

This role also enable epelrepo.

If something is missing please create a issue on [github](https://github.com/novomatic-tech/ansible-role-common-pkg)

Default Behavior
-----------------
Please check [install.yml](./tasks/install.yml)

Role Variables
--------------
common_pkg have to be defined but extra is a optional var.
All variables present here: [main.yml](./defaults/main.yml).


Example Playbook
----------------
```
- hosts: test_group
  vars:
    extra_pkgs:
      - nc
  roles:
    - novomatic-tech/common_pkg
```
 License
 -------

 MIT


Author Information
------------------

This role was created in 2018 for Novomatic Technologies Poland purposes.
