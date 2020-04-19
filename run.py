from scraper import main
import schedule
import time




if __name__ == '__main__':

    main()
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)


