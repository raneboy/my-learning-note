import hm_11_class_tutorial as my_module
from hm_11_class_tutorial import Cat

import hm_14_package

cat1 = my_module.Cat("Jerry")
cat1.eat()

cat2 = Cat("Tommy")
cat2.eat()

hm_14_package.send_message.send("Hello")
print(hm_14_package.receive_message.receive())

