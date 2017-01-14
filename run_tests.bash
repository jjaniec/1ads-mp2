#!/bin/bash

reset="\e[0m"
bold="\e[1m"
red="\e[91m"
green="\e[92m"

function cecho {
  # For text formatting with automatic reset
  echo -e "${@}" "${reset}"
}

echo -n "* Type checking... "
mypyReport=$(mypy --silent-imports src/*.py)
if [[ ${?} -eq 0 ]]; then
  cecho "${bold}${green}OK ✓"
else
  cecho "${bold}${red}Failed ✗"
  echo "${mypyReport}"
  exit 1
fi

echo -n "* Running test suite... "
cd test
for testFile in *.py; do
  testReport=$(python3 $testFile -v 2>&1)
  if [[ ${?} -ne 0 ]]; then
    cecho "${bold}${red}Failed ✗"
    echo "${testReport}"
    exit 1
  fi
done
cd ..
cecho "${bold}${green}OK ✓"
