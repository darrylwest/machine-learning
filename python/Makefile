FILES=lib/*.py
TESTFILES=tests/*.py
LINT=pylint --rcfile .pylintrc

all:
	@make test

lint:
	@( $(LINT) $(FILES) )

test:
	@( python $(TESTFILES) )
	@( echo "linting..." )
	@( make lint | tail -3)

watch:
	@( ./watcher.js )


.PHONY:	lint
.PHONY:	watch
.PHONY:	test
