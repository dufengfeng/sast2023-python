import streamlit as st
import json

def read_articles(filename):
    data=json.load(filename)
    return data

def replace(article, keys):
    for i in range(len(keys)):
        article=article.replace("{{"+str(i+1)+"}}",keys[i])
    return article

if __name__ == "__main__":

    st.title('RELAX GEME TIME')
    uploaded_file = st.file_uploader("上传JSON文件", type="json")

    if uploaded_file is not None:
        text=read_articles(uploaded_file)
        articles=text["articles"]
        list1=[]

        for one_article in articles:
            list1.append(one_article['title'])
        selected_option = st.radio("请选择一个选项：", list1)

        for one_article in articles:
            if selected_option==one_article['title']:
                article=one_article
                # st.write("succeed")

        st.write("您选择了：", selected_option)
        st.write("以下是一些提示性内容，请根据给出的提示，填写你想要填写的单词：")
        keys=[]
        a=0

        for hint in article['hints']:
            a=a+1
            value=st.text_input(hint,key=str(a))
            keys.append(value)
        new_article=replace(article['article'],keys)
        button = st.button("显示结果")

        if button:
            st.write("以下是你创造出来的文章！")
            st.write(new_article)


