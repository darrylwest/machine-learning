# FILES=src/*.py test/*.py
TESTFILES=Vector.py
LINT=pylint --errors-only --rcfile .pylintrc

all:
	@make test

lint:
	@( $(LINT) $(TESTFILES) )

test:
	@( python $(TESTFILES) )
	@( make lint )

watch:
	@( ./watcher.js )


.PHONY:	lint
.PHONY:	watch
.PHONY:	test
