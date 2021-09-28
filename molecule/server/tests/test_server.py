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
        pkgs = ["cifs-utils", "samba", "smbclient"]
    elif host.system_info.distribution in ["amzn", "fedora"]:
        pkgs = ["cifs-utils", "samba", "samba-client"]
    else:
        # Should never get here
        assert False

    for pkg in pkgs:
        assert host.package(pkg).is_installed


def test_service_enabled(host):
    """Test that Samba server is enabled."""
    service_name = None
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        service_name = "smbd"
    elif host.system_info.distribution in ["amzn", "fedora"]:
        service_name = "smb"
    else:
        # Should never get here
        assert False

    assert host.service(service_name).is_enabled


def test_guest_user(host):
    """Test that Samba guest user was created."""
    user = host.user("smbguest")
    assert user.exists
    assert user.home == "/dev/null"
    assert user.shell == "/sbin/nologin"
    assert user.gecos == "Samba guest account"
