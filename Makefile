fmt:
	black .
	isort --overwrite-in-place .
	autoflake .
