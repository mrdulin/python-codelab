import threading
import time

products = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def comsume(self):
        condition.acquire()
        if len(products) == 0:
            condition.wait()
            print('消费者：没有产品可以消费了')
        products.pop()
        print('消费者: 消费1个产品')
        print('消费者: 还能消费的产品数量为' + str(len(products)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(4)
            self.comsume()


class Producer(threading.Thread):
    def produce(self):
        condition.acquire()
        if len(products) == 10:
            condition.wait()
            print('生产者：生产的产品数量为' + str(len(products)))
            print('生产者：停止生产!')
        products.append(1)
        print('生产者：产品总数为' + str(len(products)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.produce()


producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
producer.join()
consumer.join()
