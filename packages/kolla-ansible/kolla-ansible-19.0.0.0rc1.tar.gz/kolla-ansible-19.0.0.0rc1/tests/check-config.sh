#!/bin/bash

# Check the generated configuration files.

set -o errexit

# Enable unbuffered output for Ansible in Jenkins.
export PYTHONUNBUFFERED=1

function check_config {
    # Check every file in /etc/kolla/*.
    failed=0
    expected_user=${CONFIG_OWNER_USER:-root}
    expected_group=${CONFIG_OWNER_GROUP:-root}
    # Ignore files generated by Zuul.
    for f in $(sudo find /etc/kolla \
                -not -regex /etc/kolla/config.* \
                -not -regex /etc/kolla/certificates.* \
                -not -regex /etc/kolla/octavia-certificates.* \
                -not -regex .*pem \
                -not -regex .*key \
                -not -regex ".*ca-certificates.*" \
                -not -path /etc/kolla \
                -not -path /etc/kolla/clouds.yaml \
                -not -regex .*-openrc.sh \
                -not -regex .*-openrc-system.sh \
                -not -name globals.yml \
                -not -name header \
                -not -name inventory \
                -not -name ceph-inventory \
                -not -name kolla-build.conf \
                -not -name passwords.yml \
                -not -name passwords.yml.old \
                -not -name sources.list \
                -not -name template_overrides.j2)
    do
        mode=$(sudo stat -c %a $f)
        owner=$(sudo stat -c %U:%G $f)
        if [[ -d $f ]]; then
            # Directories should be 770.
            if [[ $mode != "770" ]]; then
                failed=1
                echo "ERROR: Unexpected permissions on directory $f. Got $mode, expected 770"
            fi
        else
            # Files should be 600, 660 or 770.
            if [[ ! $mode =~ ^(600|660|770)$ ]] ; then
                failed=1
                echo "ERROR: Unexpected permissions on file $f. Got $mode, expected 770 or 660"
            fi
        fi
        # Owner user & group should be the config owner, default root.
        if [[ $owner != "$expected_user:$expected_group" ]]; then
            failed=1
            echo "ERROR: Unexpected ownership on $f. Got $owner, expected $expected_user:$expected_group"
        fi
    done
    return $failed
}

check_config
