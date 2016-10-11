FILES=lib/*.py
TESTFILES=tests/
LINT=pylint --rcfile .pylintrc
NOSE=/usr/local/bin/nosetests --cover-package=lib --with-coverage

all:
	@make test

lint:
	@( $(LINT) $(FILES) )

test:
	@( $(NOSE) $(TESTFILES) $(FILES) )
	@( echo "linting..." )
	@( make lint | tail -4 )

watch:
	@( ./watcher.js )


.PHONY:	lint
.PHONY:	watch
.PHONY:	test
