from flask_script import Manager
from api import app, mongo
import unittest


manager = Manager(app)


@manager.command
def test():
    """Run unittests."""
    mongo.db.users.remove()  # Clear db before tests.
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
