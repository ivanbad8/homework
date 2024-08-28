from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password, ):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = i

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f"Пользователь {nickname} уже существует.")
        else:
            i = User(nickname, password, age)
            self.users.append(i)
            self.log_in(i.nickname, i.password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, movie):
        video = []
        for i in self.videos:
            if movie.upper() in i.title.upper():
                video.append(i.title)
        return video

    def watch_video(self, movie):
        if self.current_user and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу.")
        elif self.current_user:
            for i in self.videos:
                if movie in i.title:
                    for v in range(1, 11):
                        print(v, end=" ")
                        sleep(1)
                    print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

    def __str__(self):
        return self.videos


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
