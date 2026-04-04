#!/bin/bash

set -uex

# Needed for some platforms
export NO_AT_BRIDGE=1

# Default list of files to lint
: "${CHANGED_FILES:=}"
if [ -z "$CHANGED_FILES" ]; then
  # Nothing to do
  exit 0
fi
rc=0
#hack: Only way to put a newline into a variable
nl='
'
delim="$nl"

# If only one file, delimiter does not matter.
if [[ "$CHANGED_FILES" == *" "* ]]; then
    delim=" "
fi

test_scripts=()
test_scripts+=("d_rats/dplatform")
test_scripts+=("d_rats/ddt2")

echo "CHANGED_FILES: $CHANGED_FILES"
for test_script in "${test_scripts[@]}"; do
    # Hack is to add a leading delimiter for a quick check to
    # see if filename is in a character delimited path
    echo "test_script: $test_script"
    if [[ "$delim$CHANGED_FILES" == *"$delim$test_script"* ]]; then
        module="${test_scripts//\//.}"
        python -m "${module}" || rc=1
    else
        echo "No script file found."
        module="${test_scripts//\//.}"
        echo "module: $module"
    fi
done
echo "final status = ${rc}"
exit "${rc}"
