from time import sleep
from datetime import datetime
def main():
    while True:
    	dt = datetime.now()
    	print(dt)
    	sleep(1000)


if __name__ == '__main__':
	main() 