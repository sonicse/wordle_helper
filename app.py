import streamlit as st

import wordle


st.title("Wordle Helper")
col1, col2, col3, col4, col5 = st.columns(5)

char_1 = col1.text_input(label="1", max_chars=1)
char_2 = col2.text_input(label="2", max_chars=1)
char_3 = col3.text_input(label="3", max_chars=1)
char_4 = col4.text_input(label="4", max_chars=1)
char_5 = col5.text_input(label="5", max_chars=1)

chars = [char_1, char_2, char_3, char_4, char_5]

exclude = st.text_input("Не совпадающие символы:", placeholder="абвгде..")
include = st.text_input("Совпадающие символы:", placeholder="жзиклмн..")

if st.button("Варианты"):
    words = wordle.words_gen("data/russian_nouns.txt")
    words = wordle.filter_words(words, exclude=exclude, include=include, chars=chars)
    words_text = "\n".join(words)
    st.text(words_text)
