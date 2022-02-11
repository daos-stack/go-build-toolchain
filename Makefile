NAME	:= go
SRC_EXT	:= gz

include packaging/Makefile_packaging.mk

clean:
	rm -fr _topdir *.tar.gz
