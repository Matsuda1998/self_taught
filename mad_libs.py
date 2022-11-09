import re
text="""キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、科学者たちは
そのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と
 __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls:文字列で、ユーザーに入力してもらいたい単語（ヒント）
    の部分は２つのアンダースコアで挟んでください。ヒントの単語には
    アンダースコアを含めないでください。
    例 \: __hint__ ⇒〇　__hint_hint__ ⇒×
    """
    hints=re.findall("__.*?__",mls)
    if hints is not  None:
        for words in hints:
            q="{}を入力 ".format(words)
            q=input(q)
            mls=mls.replace(words,q,1)
        print("\n")
        mls=mls.replace("\n","")
        print(mls)
    else:
        print("無効な引数です")
    
mad_libs(text)
