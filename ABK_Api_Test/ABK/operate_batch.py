# coding=utf-8
from ABK.create_batch import create_batch
from ABK.issue_project import issue_batch
import time


if __name__ == '__main__':
    create_user = create_batch()
    time.sleep(2)
    issue_user = issue_batch()
