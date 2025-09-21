# main.py - Assistente Virtual com PLN (Processamento de Linguagem Natural)
# Requisitos: Python 3.8+, venv, pyaudio, SpeechRecognition, gTTS, pygame, wikipedia

import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import wikipedia
import pygame
import time
from datetime import datetime

# Inicializa o mixer do pygame (para áudio)
pygame.mixer.init()

# Configuração do reconhecedor de voz
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Função para falar (Text-to-Speech usando pygame)
def speak(text):
    print(f"Assistente: {text}")
    tts = gTTS(text=text, lang='pt', slow=False)  # Voz em português brasileiro
    filename = "response.mp3"
    
    # Remove o arquivo antigo, se existir
    if os.path.exists(filename):
        os.remove(filename)
    
    # Gera o arquivo de áudio
    tts.save(filename)
    
    # Carrega e toca o áudio com pygame
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Espera até o áudio terminar de tocar
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    # Limpa o arquivo temporário
    pygame.mixer.music.unload()
    os.remove(filename)

# Função para ouvir e reconhecer voz (Speech-to-Text)
def get_audio():
    with microphone as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            speak("Não ouvi nada. Tente novamente.")
            return ""
        except sr.UnknownValueError:
            speak("Desculpe, não entendi o que você disse.")
            return ""
        except sr.RequestError:
            speak("Serviço de reconhecimento de voz indisponível no momento.")
            return ""
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return ""

# Função para responder comandos de voz
def respond(command):
    if 'youtube' in command:
        speak("O que você quer assistir no YouTube?")
        query = get_audio()
        if query:
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Aqui está o que encontrei sobre {query} no YouTube.")

    elif 'wikipedia' in command or 'pesquise na wikipedia' in command:
        speak("O que você quer pesquisar na Wikipedia?")
        query = get_audio()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2, auto_suggest=False)
                speak(f"Aqui está o que encontrei: {summary}")
            except wikipedia.exceptions.DisambiguationError:
                speak("Há várias opções. Seja mais específico.")
            except wikipedia.exceptions.PageError:
                speak("Não encontrei nenhuma página correspondente na Wikipedia.")
            except Exception:
                speak("Ocorreu um erro ao buscar na Wikipedia.")

    elif 'farmácia mais próxima' in command or 'onde fica a farmácia mais próxima' in command:
        speak("Buscando a farmácia mais próxima...")
        location = "farmácia mais próxima"
        url = f"https://www.google.com/maps/search/{location.replace(' ', '+')}"
        webbrowser.open(url)
        speak("Aqui está a farmácia mais próxima no Google Maps.")

    elif 'que horas são' in command or 'que hora é' in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"Agora são {now} horas.")

    elif 'desligar' in command or 'sair' in command or 'encerrar' in command:
        speak("Até logo! Estarei aqui quando precisar.")
        exit()

    else:
        speak("Desculpe, não entendi esse comando. Tente: 'abrir YouTube', 'pesquisar na Wikipedia' ou 'farmácia mais próxima'.")

# Função principal do assistente
def main():
    speak("Olá! Sou seu assistente virtual. Estou pronto para ajudar.")
    while True:
        command = get_audio()
        if command:
            respond(command)
        time.sleep(0.5)  # Pequena pausa para evitar sobrecarga

# Executar o assistente
if __name__ == "__main__":
    main()