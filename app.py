import streamlit as st

import wordle


st.title("Wordle Helper")
col1, col2, col3, col4, col5 = st.columns(5)

char_1 = col1.text_input(label="1", max_chars=1, key="char_1")
char_2 = col2.text_input(label="2", max_chars=1, key="char_2")
char_3 = col3.text_input(label="3", max_chars=1, key="char_3")
char_4 = col4.text_input(label="4", max_chars=1, key="char_4")
char_5 = col5.text_input(label="5", max_chars=1, key="char_5")

chars = [char_1, char_2, char_3, char_4, char_5]

exclude = st.text_input("Не совпадающие символы:", placeholder="абвгде..", key="exclude")
include = st.text_input("Совпадающие символы:", placeholder="жзиклмн..", key="include")

def clear():
    st.session_state["char_1"] = ""
    st.session_state["char_2"] = ""
    st.session_state["char_3"] = ""
    st.session_state["char_4"] = ""
    st.session_state["char_5"] = ""
    st.session_state["include"] = ""
    st.session_state["exclude"] = ""

but1, but2 = st.columns(2)

def words():
    words = wordle.words_gen("C:/Users/sonicse/.work/github/wordle_helper/data/russian_nouns.txt")
    words = wordle.filter_words(words, exclude=exclude, include=include, chars=chars)
    words_text = "\n".join(words)
    but1.text(words_text)

but1.button("Варианты", on_click=words)
but2.button("Очистить", on_click=clear)
