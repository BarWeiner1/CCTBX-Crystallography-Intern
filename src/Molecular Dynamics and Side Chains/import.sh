#!/bin/bash
for file in /Applications/cctbx-dev-1842/modules/cctbx_project; do
  if [ -f "$file" ] ; then
    . "$file"
  fi
done