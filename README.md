# ansible-role-samba #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-samba/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-samba/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-samba.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-samba/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-samba.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-samba/context:python)

This is an Ansible role that installs the dependencies necessary for
[Samba](https://www.samba.org/).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| create_guest_user | Whether or not to create a Samba guest user.  Only applies if `server` is `true`. | `false` | No |
| guest_user | The name of the Samba guest user. | `smbguest` | No |
| guest_user_groups | A list of additional groups to which the Samba guest user should belong. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| guest_user_uid | The UID to use for the Samba guest user. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| server | Whether or not to include Samba server dependencies. | `false` | No |
<!-- | required_variable | Describe its purpose. | n/a | Yes | -->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - samba
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
