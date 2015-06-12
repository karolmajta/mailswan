from invoke import task, run

@task
def test():
    run("PYTHONPATH=src python -m unittest discover -p *_test.py")
