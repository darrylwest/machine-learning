# FILES=src/*.py test/*.py
TESTFILES=Vector.py
LINT=pylint --rcfile .pylintrc

all:
	@make test

lint:
	@( $(LINT) $(TESTFILES) )

test:
	@( python $(TESTFILES) )
	@( make lint | tail -3)

watch:
	@( ./watcher.js )


.PHONY:	lint
.PHONY:	watch
.PHONY:	test
