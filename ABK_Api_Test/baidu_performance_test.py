# coding=utf-8
from locust import HttpLocust, task, TaskSet


class UserTest(TaskSet):

    # def login(self):
    #     self.client.get("https://www.baidu.com")

    # def on_start(self):
    #     self.login()

    @task
    def go_baidu(self):
        self.client.get('https://www.baidu.com')


class RunTest(HttpLocust):
    task_set = UserTest
