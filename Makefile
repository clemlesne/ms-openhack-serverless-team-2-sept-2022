init:
		pip install -r requirements.txt

black:
	black .

start:
		func start

publish:
		func azure functionapp publish fa-rating-team2-oh-fc
