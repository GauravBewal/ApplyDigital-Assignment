import random



def go_back(page):
    return page.go_back()

def sleep_for_5_seconds(page):
    return page.wait_for_timeout(5000)

def get_random_number():
    return random.randint(a=1, b=20)
