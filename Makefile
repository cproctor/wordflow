S3_BUCKET = s3://docs.makingwithcode.org/wordflow/
CF_DISTRIBUTION = EPA6NHZ2LEH1A

.PHONY: build deploy clean

build:
	$(MAKE) -C docs html

deploy: build
	aws s3 sync docs/_build/html $(S3_BUCKET)
	aws cloudfront create-invalidation --distribution-id $(CF_DISTRIBUTION) --paths "/wordflow/*"

clean:
	$(MAKE) -C docs clean
