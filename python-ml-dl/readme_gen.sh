#!/bin/bash
WORK_DIR=$1
ls ${WORK_DIR}|xargs.exe -I hello echo "[hello](./hello)" >> ${WORK_DIR}/README.md
