import speech_recognition as sr

r = sr.Recognizer()
cout = 0

def record_text():
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                meu_Texto = r.recognize_google(audio2)
                return meu_Texto

        except sr.RequestError as e:
            print(f"Deu algum problema no :{0}".format(e))
        except sr.UnknownValueError:
            print("Error desconhecido")
    return


def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    cout =+ 1
    return


while 1:
    text = record_text()
    output_text(text)
    print(f'foi usado {cout} o chat de voz')
    print("Texto, animal de tetano")
