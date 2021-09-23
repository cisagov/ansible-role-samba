"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_packages(host):
    """Ensure that all expected packages are installed."""
    pkgs = None
    if (
        host.system_info.distribution == "debian"
        or host.system_info.distribution == "kali"
        or host.system_info.distribution == "ubuntu"
    ):
        pkgs = ["samba-common"]
    elif (
        host.system_info.distribution == "fedora"
        or host.system_info.distribution == "amzn"
    ):
        pkgs = ["cifs-utils"]
    else:
        # Should never get here
        assert False

    for pkg in pkgs:
        assert host.package(pkg).is_installed