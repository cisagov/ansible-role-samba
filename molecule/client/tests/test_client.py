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
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        pkgs = ["cifs-utils", "smbclient"]
    elif host.system_info.distribution in ["amzn", "fedora"]:
        pkgs = ["cifs-utils", "samba-client"]
    else:
        # Should never get here
        assert False

    for pkg in pkgs:
        assert host.package(pkg).is_installed
