[![Build Status](https://travis-ci.org/novomatic-tech/ansible-role-common-pkg.svg?branch=master)](https://travis-ci.org/novomatic-tech/ansible-role-common-pkg) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role Name](https://img.shields.io/ansible/role/29052.svg)](https://galaxy.ansible.com/novomatic-tech/common_pkgs/) [![Ansible Role counter](https://img.shields.io/ansible/role/d/29052.svg)](https://galaxy.ansible.com/novomatic-tech/common_pkgs/)

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
      - name: nc
      - state: present
  roles:
    - novomatic-tech/common_pkgs
```
 License
 -------

 MIT


Author Information
------------------

This role was created in 2018 for Novomatic Technologies Poland purposes.
