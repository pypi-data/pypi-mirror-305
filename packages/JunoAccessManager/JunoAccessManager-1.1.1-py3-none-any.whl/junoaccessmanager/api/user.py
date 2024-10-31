import logging
import requests
from pulsar import Client, AuthenticationToken, ConsumerType

logger = logging.getLogger('pulsar_client_logger')
logger.setLevel(logging.ERROR)  # 设置日志级别为 ERROR 或更高


# def pulsar_consumer(topic_name, subscription_name):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # 创建客户端
#             client = Client(
#                 service_url=self.__pulsar_host,
#                 authentication=AuthenticationToken(self.__pulsar_token)
#             )
#
#             # 创建消费者
#             consumer = client.subscribe(topic_name, subscription_name,
#                                         consumer_type=ConsumerType.Shared,
#                                         message_listener=lambda msg: process_message(msg, func))
#
#             try:
#                 print(f"Listening on topic: {topic_name}")
#                 while True:
#                     # 消费者会自动监听消息，这里只是让主循环持续运行
#                     time.sleep(1)
#             except KeyboardInterrupt:
#                 print('Stopping consumer...')
#             finally:
#                 # 关闭资源
#                 consumer.close()
#                 client.close()
#
#         def process_message(msg, handler):
#             try:
#                 print(f"Received message id={msg.message_id()}, data={msg.data()}, properties={msg.properties()}")
#                 # 确认消息
#                 msg.ack()
#                 # 调用消息处理函数
#                 handler(msg.data(), *msg.properties())
#             except Exception as e:
#                 print(f"Failed to process message: {e}")
#                 # 如果处理失败，可以选择重新传递消息
#                 msg.redeliverLater()
#
#         return wrapper
#
#     return decorator


class JAMClient:
    def __init__(self, manager_host: str, pulsar_host: str, username: str, password: str):
        self.__access_token: str = ''
        self.__pulsar_token: str = ''
        self.__manager_host: str = manager_host
        self.__pulsar_host: str = pulsar_host
        self.__username: str = username
        self.__password: str = password

    def connect(self):
        url = f"{self.__manager_host}/api/user/me/login"
        body = {
            'username': self.__username,
            'password': self.__password
        }
        resp = requests.post(url=url, data=body, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                self.__access_token = resp.json()['data']['access_token']
                self.__pulsar_token = self.account_info()['mq_token']
                return True
            elif resp.json()['code'] == 400:
                raise ConnectionRefusedError
        else:
            raise ConnectionError

    def disconnect(self):
        self.__access_token = ''

    def update_account(self, email: str = None, phone: str = None):
        if self.__access_token == '':
            raise ConnectionRefusedError

        url = f"{self.__manager_host}/api/user/me/update"
        url = f"{url}?username={self.__username}&password={self.__password}"
        header = {'Authorization': f'Bearer {self.__access_token}'}
        if email or phone:
            url = f'{url}&'
            if email:
                url = f'{url}email={email}'
            if phone:
                url = f'{url}phone={phone}'
        resp = requests.post(url=url, headers=header, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                return True
            else:
                raise ConnectionRefusedError
        else:
            raise ConnectionRefusedError

    def account_info(self):
        if self.__access_token == '':
            raise ConnectionRefusedError

        url = f"{self.__manager_host}/api/user/me"
        header = {'Authorization': f'Bearer {self.__access_token}'}
        resp = requests.get(url=url, headers=header, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                return resp.json()['data']
            else:
                raise ConnectionRefusedError
        else:
            raise ConnectionRefusedError

    def my_permissions(self):
        if self.__access_token == '':
            raise ConnectionRefusedError

        url = f"{self.__manager_host}/api/permission/me"
        header = {'Authorization': f'Bearer {self.__access_token}'}
        resp = requests.get(url=url, headers=header, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                return resp.json()['data']
            elif resp.json()['code'] == 400:
                return resp.json()['msg']
            else:
                raise ConnectionRefusedError
        else:
            raise ConnectionRefusedError

    def my_permissions_in_namespace(self, tenant: str, namespace: str):
        if self.__access_token == '':
            raise ConnectionRefusedError

        url = f"{self.__manager_host}/api/permission/me/{tenant}/{namespace}"
        header = {'Authorization': f'Bearer {self.__access_token}'}
        resp = requests.get(url=url, headers=header, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                return resp.json()['data']
            elif resp.json()['code'] == 400:
                return resp.json()['msg']
            else:
                raise ConnectionRefusedError
        else:
            raise ConnectionRefusedError

    def my_permissions_in_namespace_topic(self, tenant: str, namespace: str, topic: str):
        if self.__access_token == '':
            raise ConnectionRefusedError

        url = f"{self.__manager_host}/api/permission/me/{tenant}/{namespace}/{topic}"
        header = {'Authorization': f'Bearer {self.__access_token}'}
        resp = requests.get(url=url, headers=header, timeout=10)
        if resp.status_code == 200:
            if resp.json()['code'] == 200:
                return resp.json()['data']
            elif resp.json()['code'] == 400:
                return resp.json()['msg']
            else:
                raise ConnectionRefusedError
        else:
            raise ConnectionRefusedError

    def produce(self, msg: str, tenant: str, namespace: str, topic: str):
        pulsar_client = Client(
            service_url=self.__pulsar_host,
            authentication=AuthenticationToken(self.__pulsar_token)
        )
        producer = pulsar_client.create_producer(topic=f'persistent://{tenant}/{namespace}/{topic}')
        producer.send(msg.encode('utf-8'))
        producer.close()
        pulsar_client.close()

    def do_consume(self, tenant: str, namespace: str, topic: str, subscription: str):
        self.pulsar_client = Client(
            service_url=self.__pulsar_host,
            authentication=AuthenticationToken(self.__pulsar_token),
            logger=logger
        )
        consumer = self.pulsar_client.subscribe(
            topic=f'persistent://{tenant}/{namespace}/{topic}',
            subscription_name=subscription,
            consumer_type=ConsumerType.Shared
        )
        msg = consumer.receive()
        consumer.acknowledge(msg)
        consumer.close()
        # self.pulsar_client.close()
        return msg.data().decode('utf-8')

    def consume(self, tenant: str, namespace: str, topic: str, subscription: str, func):
        while True:
            msg = self.do_consume(tenant, namespace, topic, subscription)
            func(msg)







