FILES=lib/*.py
TESTFILES=tests/*.py
LINT=pylint --rcfile .pylintrc
NOSE=/usr/local/bin/nosetests

all:
	@make test

lint:
	@( $(LINT) $(FILES) )

test:
	@( nosetests $(TESTFILES) )
	@( echo "linting..." )
	@( make lint | tail -4 )

watch:
	@( ./watcher.js )


.PHONY:	lint
.PHONY:	watch
.PHONY:	test
