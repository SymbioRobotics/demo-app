# Unlike all other Makefiles in the repo, this one defines no goals of its own.
# Delegate all COMMON_GOALS to the subdirectories of the current environment.

default: all

include infrastructure/common.mk

# Compute the list of subdirectories using the output of bootstrap.

SUBDIRS = app ui

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

$(COMMON_GOALS): $(SUBDIRS)
