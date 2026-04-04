#!/usr/bin/env bash

git filter-repo --replace-text <(cat <<EOF
AKIA==>REMOVED
aws_secret_access_key==>REMOVED
SECRET==>REMOVED
TOKEN==>REMOVED
PASSWORD==>REMOVED
EOF
)
