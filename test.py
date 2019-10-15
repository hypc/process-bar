from time import sleep

from process_bar import ProcessBar

if __name__ == '__main__':
    p = ProcessBar(143, msg='123')
    p.begin()
    for i in range(143):
        sleep(0.02)  # process ...
        p.print(i + 1)
    p.end()
