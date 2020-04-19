from scraper import main
import schedule
import time




if __name__ == '__main__':

    # Runs main() every 5 hours
    # You can change the amount of time and time interval by tweaking the "schedule.ever()..."
    main()
    schedule.every(5).hours.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)


