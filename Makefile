# SPDX-License-Identifier: BSD-2-Clause-Patent
# Copyright (c) 2022-2024 Intel Corporation

NAME	:= go
SRC_EXT	:= gz

include packaging/Makefile_packaging.mk

clean:
	rm -fr _topdir *.tar.gz

sync_packaging:
	rsync -aP --delete ../packaging/ ./packaging/ \
		--exclude=.git \
		--exclude=Makefile \
		--exclude=README.md \
		--exclude=packaging \
		--exclude=Jenkinsfile \
		--exclude=install
