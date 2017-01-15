#!/bin/bash

base_dir=$(dirname ${0})
export PYTHONPATH=${base_dir}/src:${PYTHONPATH}
files_to_typecheck=(basis.py possible.py merge.py)

reset="\e[0m"
bold="\e[1m"
red="\e[91m"
green="\e[92m"

echo -n "* Type checking... "
mypyReport=$(mypy --silent-imports ${base_dir}/src/${files_to_typecheck})
if [[ ${?} -eq 0 ]]; then
  echo -e "${bold}${green}OK ✓${reset}"
else
  echo -e "${bold}${red}Failed ✗${reset}"
  echo "${mypyReport}"
  exit 1
fi

echo -n "* Running test suite... "
for testFile in ${base_dir}/test/*.py; do
  testReport=$(python3 $testFile -v 2>&1)
  if [[ ${?} -ne 0 ]]; then
    echo -e "${bold}${red}Failed ✗${reset}"
    echo "${testReport}"
    exit 1
  fi
done
echo -e "${bold}${green}OK ✓${reset}"
