import time
import datetime
import requests
from functools import wraps
import traceback
import threading

commander = threading.Condition()


def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return _singleton_wrapper


class BaseProxiedSession:
    """
    单线程代理基类
    """
    words = None
    proxy_pool_ip = None

    def __init__(self, max_retry=2):
        super().__init__()
        # self.proxy_ip = '125.105.227.237:42046'
        self.proxy_ip = requests.get(self.proxy_pool_ip).text
        print(f'{self.words}，当前代理ip地址为：{self.proxy_ip}')
        self.retry_counter = 0
        self.max_retry = max_retry

    def get(self, *args, timeout=60, **kwargs):
        """
        经过代理的get请求，如果代理失效会自动重新获取代理，尝试max_retry次数都失败后会
        中断退出
        :param timeout:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            resp = requests.get(*args, **kwargs, proxies={'https': self.proxy_ip}, timeout=timeout)
            self.retry_counter = 0
            return resp
        except (requests.exceptions.ProxyError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError):
            """
            requests.exceptions.ProxyError:发送请求时代理已失效
            requests.exceptions.ReadTimeout:发送请求时代理未失效，响应时已失效
            requests.exceptions.ConnectionError:连接导致的中断，可能存在代理ip的问题，所以也需要更换代理Ip
            """
            if self.retry_counter - 1 >= self.max_retry:
                self.retry_counter = 0
                raise RecursionError(f'代理ip更新重试超过{self.max_retry}次，自动终止')
            self.proxy_ip = requests.get(self.proxy_pool_ip).text
            print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
            self.retry_counter += 1
            return self.get(*args, timeout=timeout, **kwargs)


    def post(self, *args, timeout=60, **kwargs):
        """
        经过代理的post请求，如果代理失效会自动重新获取代理，尝试max_retry次数都失败后会
        中断退出
        :param timeout:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            resp = requests.post(*args, **kwargs, proxies={'https': self.proxy_ip}, timeout=timeout)
            self.retry_counter = 0
            return resp
        except (requests.exceptions.ProxyError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError):
            if self.retry_counter - 1 >= self.max_retry:
                self.retry_counter = 0
                raise RecursionError(f'代理ip更新重试超过{self.max_retry}次，自动终止')
            self.proxy_ip = requests.get(self.proxy_pool_ip).text
            print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
            self.retry_counter += 1
            return self.post(*args, timeout=timeout, **kwargs)


class BaseMultiThreadProxiedSession(requests.Session):
    """
    多线程使用代理，自动更换代理的基类，（未测试）
    """
    words = None
    proxy_pool_ip = None

    def __init__(self, max_retry=2):
        super().__init__()
        # self.proxy_ip = '125.105.227.237:42046'
        self.proxy_ip = self.get(self.proxy_pool_ip).text
        print(f'{self.words}，当前代理ip地址为：{self.proxy_ip}')
        self.max_retry = max_retry
        self.state = 'working'
        self.thread_info = {}

    def proxied_get(self, *args, timeout=60, **kwargs):
        """
        经过代理的get请求，如果代理失效会自动重新获取代理，尝试max_retry次数都失败后会
        中断退出
        :param timeout:
        :param args:
        :param kwargs:
        :return:
        """
        # 初始化thread_info
        if threading.get_ident() not in self.thread_info:
            self.thread_info[threading.get_ident()] = {}
        try:
            if self.state == 'repairing':
                # 已有线程在进行ip更新的请求，则其他所有线程都在此等候唤醒
                commander.wait()
            resp = self.get(*args, **kwargs, proxies={'https': self.proxy_ip}, timeout=timeout)
            self.thread_info[threading.get_ident()]['retry_counter'] = 0
            self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
            return resp

        except requests.exceptions.ProxyError:
            """
            requests.exceptions.ProxyError:发送请求时代理已失效
            失效是即时失效，表明当前代理ip地址已过期，所以直接更新代理ip地址
            """
            if self.thread_info[threading.get_ident()]['retry_counter'] - 1 >= self.max_retry:
                self.thread_info[threading.get_ident()]['retry_counter'] = 0
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
                print(f'代理ip更新重试超过{self.max_retry}次，自动终止')
                return
            if self.state == 'working':
                self.state = 'repairing'
                self.proxy_ip = self.get(self.proxy_pool_ip).text
                self.state = 'working'
                self.thread_info[threading.get_ident()]['update_time'] = time.time()
                print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
                commander.notifyAll()
                self.thread_info[threading.get_ident()]['retry_counter'] += 1
            return self.proxied_get(*args, timeout=timeout, **kwargs)

        except requests.exceptions.ReadTimeout:
            """
            requests.exceptions.ReadTimeout:发送请求时代理未失效，响应时已失效
            由于失效是超时失效，有可能已经被其他线程更新了代理Ip地址，所以超时失效不做代理ip地址的更新操作
            """
            return self.proxied_get(*args, timeout=timeout, **kwargs)

        except requests.exceptions.ConnectionError:
            """
            requests.exceptions.ConnectionError:连接导致的中断，可能存在代理ip的问题，所以也需要更新代理Ip
            但不是每次都更新，累计三次ConnectionError才会更新，不考虑其他线程更新情况
            """
            if "conn_retry_counter" not in self.thread_info[threading.get_ident()]:
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
            if self.thread_info[threading.get_ident()]['retry_counter'] - 1 >= self.max_retry:
                self.thread_info[threading.get_ident()]['retry_counter'] = 0
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
                print(f'代理ip更新重试超过{self.max_retry}次，自动终止')
                return
            if self.thread_info[threading.get_ident()]["conn_retry_counter"] == 3:
                if self.state == 'working':
                    self.state = 'repairing'
                    self.proxy_ip = self.get(self.proxy_pool_ip).text
                    self.state = 'working'
                    print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
                    commander.notifyAll()
                    self.thread_info[threading.get_ident()]['retry_counter'] += 1
                    self.thread_info[threading.get_ident()]["conn_retry_counter"] += 1
            return self.proxied_get(*args, timeout=timeout, **kwargs)


    def proxied_post(self, *args, timeout=60, **kwargs):
        """
        经过代理的post请求，如果代理失效会自动重新获取代理，尝试max_retry次数都失败后会
        中断退出
        :param timeout:
        :param args:
        :param kwargs:
        :return:
        """
        # 初始化thread_info
        if threading.get_ident() not in self.thread_info:
            self.thread_info[threading.get_ident()] = {}
        try:
            if self.state == 'repairing':
                commander.wait()
            resp = self.post(*args, **kwargs, proxies={'https': self.proxy_ip}, timeout=timeout)
            self.thread_info[threading.get_ident()]['retry_counter'] = 0
            self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
            return resp
        
        except requests.exceptions.ProxyError:
            if self.thread_info[threading.get_ident()]['retry_counter'] - 1 >= self.max_retry:
                self.thread_info[threading.get_ident()]['retry_counter'] = 0
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
                print(f'代理ip更新重试超过{self.max_retry}次，自动终止')
                return
            if self.state == 'working':
                self.state = 'repairing'
                self.proxy_ip = self.get(self.proxy_pool_ip).text
                self.thread_info[threading.get_ident()]['update_time'] = time.time()
                self.state = 'working'
                print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
                commander.notifyAll()
                self.thread_info[threading.get_ident()]['retry_counter'] += 1
            return self.proxied_post(*args, timeout=timeout, **kwargs)
        
        except requests.exceptions.ReadTimeout:
            return self.proxied_post(*args, timeout=timeout, **kwargs)
        
        except requests.exceptions.ConnectionError:
            if "conn_retry_counter" not in self.thread_info[threading.get_ident()]:
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
            if self.thread_info[threading.get_ident()]['retry_counter'] - 1 >= self.max_retry:
                self.thread_info[threading.get_ident()]['retry_counter'] = 0
                self.thread_info[threading.get_ident()]['conn_retry_counter'] = 0
                print(f'代理ip更新重试超过{self.max_retry}次，自动终止')
                return
            if self.thread_info[threading.get_ident()]["conn_retry_counter"] == 3:
                if self.state == 'working':
                    self.state = 'repairing'
                    self.proxy_ip = self.get(self.proxy_pool_ip).text
                    self.state = 'working'
                    print(f'原代理ip地址失效，代理ip地址已更新，{self.words}，当前代理ip地址为：{self.proxy_ip}')
                    commander.notifyAll()
                    self.thread_info[threading.get_ident()]['retry_counter'] += 1
                    self.thread_info[threading.get_ident()]["conn_retry_counter"] += 1
            return self.proxied_post(*args, timeout=timeout, **kwargs)


@Singleton
class Ent_01_Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6712634735433564&sign=487e01568fd2a992729c590fc9dc8311'
    words = '正在使用企业级1分钟代理'


@Singleton
class Ent_03_Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6156636289833618&sign=517044859996a5558af5a6f8e889d719'
    words = '正在使用企业级3分钟代理'


@Singleton
class Ent_05_Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6402286667599452&sign=e79f9242447459c2fcb619ae8e9ffba2'
    words = '正在使用企业级5分钟代理'


@Singleton
class Ent_10_Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6110053615967745&sign=dc6e78e6e3312045a0b23b4d99069090'
    words = '正在使用企业级10分钟代理'


@Singleton
class Ent_30_Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/company/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6848239054724573&sign=ece44a34c99a627e8996faec0a1b09eb'
    words = '正在使用企业级30分钟代理'


@Singleton
class Ind01_03Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6234339221717509&sign=cae5eaa9859c337cca907b35a86d4912'
    words = '正在使用私人1-3分钟代理'


@Singleton
class Ind01_05Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6130555184884104&sign=1229951fd50bec0145974d38b9c85d48'
    words = '正在使用私人1-5分钟代理'


@Singleton
class Ind05_10Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6840461001322271&sign=5fe0df8eda72e4e1bd6ae882707eef52'
    words = '正在使用私人5-10分钟代理'


@Singleton
class Ind10_30Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6703864181189056&sign=06a6e70047d421350896f514f73f634f'
    words = '正在使用私人10-30分钟代理'


@Singleton
class Ind30_60Session(BaseProxiedSession):
    proxy_pool_ip = 'http://v2.api.juliangip.com/postpay/getips?num=1&pt=1&result_type=text&split=1&trade_no=6361691914388459&sign=681224a4d9b31d67d0d3499178d4ae4e'
    words = '正在使用私人30-60分钟代理'
