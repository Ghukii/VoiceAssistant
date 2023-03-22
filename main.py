import speech_recognition
import subprocess
import keyboard
from pygame import mixer
import webbrowser
import pyttsx3
import os
import datetime

mixer.init()
mixer.music.load("sound.mp3")


class VoiceAssistant:
    def __init__(self):

        self.sr = speech_recognition.Recognizer()

        self.application_paths = {'steam': 'C:/Program Files (x86)/Steam/steam.exe',
                                  'кружочки': 'D:/osu!/osu!.exe',
                                  'dota': 'D:/SteamLibrary/steamapps/common/dota 2 beta/game/bin/win64/dota2.exe',
                                  'браузер': 'C:/Program Files/Mozilla Firefox/firefox.exe',
                                  'discord': 'C:/Users/andrew/AppData/Local/Discord/app-1.0.9004/Discord.exe',
                                  'танки': 'D:/Games/Wargaming.net/GameCenter/wgc.exe',
                                  'telegram': 'C:/Users/andrew/AppData/Roaming/Telegram Desktop/Telegram.exe'}

        self.urls = {'youtube': 'https://www.youtube.com/',
                     'вк': 'https://vk.com/feed'}

        self.name = 'хэнк'

        self.login = 'login'
        self.password = 'password'

        self.assistant_voice = pyttsx3.init()
        self.assistant_voice.setProperty('voice', 'ru')

        self.shutdowntime = None
        self.time_now = datetime.datetime.now()

    def open(self, application):
        if application in self.application_paths: subprocess.Popen(self.application_paths[application], shell=True)
        if application in self.urls: webbrowser.open(self.urls[application])
        self.run_voice('выполнено!')

    def run_voice(self, text_to_speech):
        self.assistant_voice.say(text_to_speech)
        self.assistant_voice.runAndWait()

    def listen(self):
        with speech_recognition.Microphone() as mic:
            self.sr.adjust_for_ambient_noise(source=mic, duration=1)
            print('Start recording')
            try:
                audio = self.sr.listen(source=mic)

            except speech_recognition.UnknownValueError:
                self.run_voice('Проверьте свой микрофон!')
                return

            try:

                query = self.sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                print('Stop recording')
                print(query)
                return query

            except speech_recognition.UnknownValueError:
                pass

    def commands(self, command):

        try:
            command = command.split()

        except:
            self.assistant_voice.say('повторите команду')
            self.commands(self.listen())

        match command[0]:
            case 'открой':
                VoiceAssistant().open(command[-1])

            case 'введи':
                match command[1]:
                    case 'логин':
                        keyboard.write(self.login)
                    case 'пароль':
                        keyboard.write(self.password)
            case 'покажи':
                match command[1]:
                    case 'аниме':
                        subprocess.Popen(['notepad.exe',
                                          'C:/Users/andrew/PycharmProjects/VoiceAssistant/Anime_list.txt'])

            case 'панель':
                if command == ['панель', 'задач']:
                    keyboard.press_and_release('win')
                    self.run_voice('панель задач успешно открыта!')

            case 'загугли':
                webbrowser.open('http://google.com/search?q=' + ' '.join(command[1:]))
                self.run_voice('Запрос успешно выполнен')

            case 'включи':
                webbrowser.open('http://youtube.com/search?q=' + ' '.join(command[1:]))


if __name__ == '__main__':
    speech = VoiceAssistant()
    while True:
        inp = speech.listen()
        if inp == speech.name:
            mixer.music.play()
            speech.commands(speech.listen())
