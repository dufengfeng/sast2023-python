import argparse
import json
import sys
import random
def parser_data():
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )
    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-a","--artic",help="题库中的某一篇具体文章",required=False)
    args = parser.parse_args()
    return args

def read_articles(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data=json.load(f)
    return data

def get_inputs(hints):
    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        value=input()
        keys.append(value)
    return keys

def replace(article, keys):
    for i in range(len(keys)):
        article=article.replace("{{"+str(i+1)+"}}",keys[i])
    return article

if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    if args.artic is not None:
        for one_article in articles:
            if one_article['title'] ==args.artic:
                article=one_article
    else:
        article=random.choice(articles)

    key_s=get_inputs(article['hints'])
    #这里一定要主语article它本身是一个字典型的对象，并不是字符串
    #所以我们调用的时候要写article['article']
    new_article=replace(article['article'],key_s)
    #这里返回的是一个对象，所以千万不能以为replace函数直接进行了修改
    print(new_article)



