from instapy import InstaPy

session=InstaPy(username="robotudiatest", password="b2vva6dso", headless_browser=True).login()
session.like_by_tags(["praia", "roupas"], amount=1)
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=100)
session.set_comments(["Bacana!", ":muscle:", "Top :heart_eyes:"])
session.end()