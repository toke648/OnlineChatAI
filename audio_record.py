import speech_recognition as sr

def record(recognizer, language='en-US'):
    with sr.Microphone() as source:
        # 调整麦克风参数以减少环境噪音
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.5

        try:
            # 减少超时时间，提高响应速度
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language=language)

            print(f"You told: {text}")
            return text
        except sr.UnknownValueError:
            print('Can not understand audio')
            return
        except sr.WaitTimeoutError:
            print('No Sound detected')
            return
        except sr.RequestError as e:
            print(f"Identification service error: {e}")
            return


# import speech_recognition as sr 

# # 初始化识别器 

# recognizer = sr.Recognizer() 

# # 打开麦克风录音 

# with sr.Microphone() as source: 

#    print("请说话，我正在听...") 

#    audio = recognizer.listen(source) 

# # 将语音转文字 

# try: 

#    text = recognizer.recognize_google(audio, language="zh-CN") 

#    print(f"你刚才说的是：{text}") 

# except sr.UnknownValueError: 

#    print("抱歉，我听不懂你刚才说的话！") 

# except sr.RequestError: 

#    print("无法连接到语音识别服务，请检查网络！")
