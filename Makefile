fmt:
	black .
	isort --overwrite-in-place .
	autoflake --remove-all-unused-imports -i -r .
