import os

badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = "84cae48c4a7a261844abf94cc9925b90605fda00"

os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run python3.10 manage.py test')
os.system('git bisect reset')