#!/bin/bash
set -eE -o functrace

failure() {
  local lineno=$1
  local msg=$2
  echo "Failed at $lineno: $msg"
}
trap 'failure ${LINENO} "$BASH_COMMAND"' ERR

WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/.."

set -o pipefail

main(){
  cd ${WORKDIR}

  pip3 install --upgrade virtualenv
  mkdir -pv .venv
  python3 -m virtualenv .venv

  # shellcheck disable=SC1091
  source .venv/bin/activate

  pip3 install -r requirements.txt
  python -m pre_commit autoupdate
  python -m pre_commit install
  python -m pre_commit run --all-files
}

main "$@"
