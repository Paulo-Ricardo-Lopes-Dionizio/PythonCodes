import speech_recognition as sr
r = sr.Recognizer()
def gravar_texto():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)
                audio2 = r.listen(source2)
                meuTexto = r.recognize_google(audio2)
                return meuTexto

        except sr.RequestError as e:
          print("Deu algum problema;{0}".format(e))
        except sr.UnknownValueError:
          print("Erro desconhecido")
    return
def sair_texto(text):
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return
while (1):
    text = gravar_texto()
    sair_texto(text)
    print("Texto, animal de tetano")