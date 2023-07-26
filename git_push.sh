#!/usr/bin/bash
git push origin master -c credential.helper= \
  -c credential.helper='!f() { echo username=hamdan.hy@gmail.com; echo "password=$GITHUB_TOKEN"; };f'
