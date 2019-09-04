# coding=utf-8
from locust import HttpLocust, TaskSet, task


# 性能测试脚本初步编写
class UserLoanTest(TaskSet):
    """
    继承TaskSet,创建测试任务类
    """
    def login(self):
        """
        登陆实例方法
        :return:
        """
        self.client.post("http://localhost:8088/users/login/",
                         {"user_account": "admin", "password": "123456"})

    def logout(self):
        self.client.get("http://localhost:8088/users/logout/")

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    # 添加事务
    @task
    def user_index(self):
        self.client.get("http://localhost:8088/users/")


class RunLoadTests(HttpLocust):
    """
    运行性能测试类
    """
    task_set = UserLoanTest
