import pytest
from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("common_pkgs", [
    "curl",
    "tcpdump",
    "git",
    "htop"
])
def test_common(host, common_pkgs):
    c = host.package(common_pkgs)
    assert c.is_installed


@pytest.mark.parametrize("extra_pkgs", [
    "nmap"
])
def test_extra(host, extra_pkgs):
    c = host.package(extra_pkgs)
    assert c.is_installed
