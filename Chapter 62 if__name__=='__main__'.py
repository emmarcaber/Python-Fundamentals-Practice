# CHAPTER 62
# if __name__ == '__main__'

# y tho?
# 1. Module can be run as standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code and found within __main__

import module_two

module_two.hello()

if __name__ == '__main__':
    print(__name__)
    print(module_two.__name__)