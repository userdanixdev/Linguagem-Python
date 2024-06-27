# Criar um projeto em Python relacionado ao metalcore pode ser uma experiência interessante e divertida!
#  Podemos desenvolver um projeto que analise letras de músicas de bandas de metalcore,
#  extraindo palavras-chave, realizando análises de sentimento e até mesmo criando gráficos
#  para visualizar os dados. Aqui está um esboço para um projeto chamado "Metalcore Lyrics Analyzer":

# Metalcore Lyrics Analyzer:
# Objetivo:
# Analisar letras de músicas de bandas de metalcore para extrair informações relevantes,
#  como palavras-chave, frequência de palavras, e realizar análises de sentimento.
#  Além disso, gerar visualizações gráficas desses dados.

# Funcionalidades:
# Coleta de Letras de Músicas:

# Obter letras de músicas de bandas de metalcore através de APIs (por exemplo, Genius API) ou scraping.

# Processamento de Texto:

# Limpeza de dados (remoção de stop words, pontuações, etc.).
# Tokenização de palavras.

# Análise de Palavras-Chave:

# Extração e contagem de palavras-chave.
# Identificação de palavras mais frequentes.

# Análise de Sentimento:

# Classificação das letras quanto ao sentimento (positivo, negativo, neutro) usando bibliotecas como NLTK ou TextBlob.

# Visualizações:

# Gráficos de frequência de palavras.
# Nuvens de palavras (word clouds).
# Gráficos de sentimento.

# Interface de Usuário:

# Interface de linha de comando (CLI) para interação com o usuário.


#Estrutura do Projeto:
#Coleta de Dados:

#data_collection.py
#Funções para coletar letras de músicas de APIs ou scraping.

#Processamento de Texto:
#text_processing.py
#Funções para limpeza e tokenização de texto.

#Análise de Dados:
#data_analysis.py
#Funções para análise de palavras-chave e sentimentos.

#Visualizações:
#visualizations.py
#Funções para gerar gráficos e nuvens de palavras.
#Interface de Usuário:

#main.py
#Função principal para interação com o usuário.

#############################################################################
#Coleta de Dados:

#data_collection.py
#Funções para coletar letras de músicas de APIs ou scraping.

import requests

def get_lyrics_from_genius(song_title, artist_name, genius_api_key):
    base_url = "https://api.genius.com"
    headers = {'Authorization': f'Bearer {genius_api_key}'}
    search_url = f'{base_url}/search'
    data = {'q': f'{song_title} {artist_name}'}
    response = requests.get(search_url, headers=headers, data=data)
    json_response = response.json()
    remote_song_info = None
    for hit in json_response['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        return song_url
    return None

def get_song_lyrics(url):
    page = requests.get(url)
    from bs4 import BeautifulSoup
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find("div", class_="lyrics")
    if lyrics:
        return lyrics.get_text()
    return None
########################################################################################
#Processamento de Texto:
#text_processing.py
#Funções para limpeza e tokenização de texto.

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[\r\n]+', ' ', text)
    text = re.sub(r'\W', ' ', text)
    return text

def tokenize_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text
############################################################################################

#Análise de Dados:
#data_analysis.py
#Funções para análise de palavras-chave e sentimentos.

from collections import Counter
from textblob import TextBlob

def get_word_frequency(tokenized_text):
    return Counter(tokenized_text)

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

#################################################################################################
#Visualizações:
#visualizations.py
#Funções para gerar gráficos e nuvens de palavras.
#Interface de Usuário:

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_word_frequency(word_freq):
    words = list(word_freq.keys())
    counts = list(word_freq.values())
    plt.bar(words[:10], counts[:10])
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Words by Frequency')
    plt.show()

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
######################################################################################################
#main.py
#Função principal para interação com o usuário.

from data_collection import get_lyrics_from_genius, get_song_lyrics
from text_processing import clean_text, tokenize_text
from data_analysis import get_word_frequency, analyze_sentiment
from visualizations import plot_word_frequency, generate_wordcloud

def main():
    genius_api_key = 'YOUR_GENIUS_API_KEY'
    song_title = input('Enter the song title: ')
    artist_name = input('Enter the artist name: ')

    song_url = get_lyrics_from_genius(song_title, artist_name, genius_api_key)
    if not song_url:
        print('Song not found.')
        return

    lyrics = get_song_lyrics(song_url)
    if not lyrics:
        print('Could not retrieve lyrics.')
        return

    cleaned_text = clean_text(lyrics)
    tokenized_text = tokenize_text(cleaned_text)

    word_freq = get_word_frequency(tokenized_text)
    sentiment = analyze_sentiment(cleaned_text)

    print(f'Sentiment Polarity: {sentiment}')
    plot_word_frequency(word_freq)
    generate_wordcloud(cleaned_text)

if __name__ == "__main__":
    main()
################################################################################################
#Notas:
# Genius API Key: Você precisa de uma chave API do Genius. 
# Você pode obter uma criando uma conta no Genius e registrando uma nova aplicação.
#Bibliotecas: Certifique-se de ter as bibliotecas necessárias instaladas 
# (requests, beautifulsoup4, nltk, textblob, matplotlib, wordcloud). Você pode instalá-las usando pip.
