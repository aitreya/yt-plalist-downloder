try:
    from selenium import webdriver
except ModuleNotFoundError as E:
    print(f"selenium not found")
try:
    from webdriver_manager.chrome import ChromeDriverManager
except ModuleNotFoundError as E:
    print(f"webdriver_manager not found")
from math import ceil
from time import sleep

with open('components/javascript/get_video_list.js') as f:
    sc = f.read()
with open('components/javascript/number_of_videos.js') as f:
    v_num_js = f.read()


class Playlist:

    def __init__(self, url):
        self.is_downloadable = False
        self.total_videos = '0 videos'
        self.playlist_url = url
        self.playlist_name, self.playlist_videos = self.some_details()
        self.playlist_duration = []
        if self.total_videos != 0:
            self.success_rate = (len(self.playlist_videos) / self.total_videos) * 100

    def some_details(self):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            print(e)
            exit(code='Chrome driver not found !!!')
        else:
            try:
                driver.get(self.playlist_url)
            except:
                print("Unable to open link for whatever reason")
                exit(code="Not supported Youtube Link. \nExiting ...")
            else:
                title = driver.execute_script("return document.title")
                try:
                    self.total_videos = driver.execute_script(f"return {v_num_js}")
                except Exception as e:
                    pass
                self.total_videos = self.return_num(self.total_videos)
                self.is_downloadable_playlist()
                if self.is_downloadable:
                    self.scroller(self.total_videos, driver)
                    data = driver.execute_script(f"return {sc}")
                    data = [i for i in data if i is not None]
                else:
                    data = 'No videos'
                return title, data
            finally:
                driver.close()

    def is_downloadable_playlist(self):
        if self.total_videos > 0:
            self.is_downloadable = True

    @staticmethod
    def scroller(num, driver):
        mul = ceil(num / 100)
        if mul > 1:
            print("Scrolling ...", end='\t')
        for i in range(1, mul):
            driver.execute_script('window.scrollBy(0,50000)')
            sleep(0.1)
            y_before = driver.execute_script('return window.pageYOffset')
            for j in range(30):
                if j == 29:
                    print('Done')
                    return
                sleep(1)
                driver.execute_script('window.scrollBy(0,1)')
                y_after = driver.execute_script('return window.pageYOffset')
                if y_before < y_after:
                    sleep(2)
                    break
        print('Done')

    @staticmethod
    def return_num(string):
        if ',' in string:
            a = string.split(' ')[0]
            a = a.split(',')
            a = ''.join(a)
            return int(a)
        else:
            return int(string.split(' ')[0])


if __name__ == '__main__':
    yt = Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
    print(yt.__dict__)
    print(len(yt.playlist_videos))