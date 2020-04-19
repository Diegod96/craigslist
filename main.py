import time
from scraper import main
import schedule



if __name__ == '__main__':
    main()

    schedule.every(1).hours.do(main)

    while 1:
        schedule.run_pending()
        time.sleep(1)
