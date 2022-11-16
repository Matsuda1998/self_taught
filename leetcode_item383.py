"""leetcode.comの初めての人への３問目"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_ransomNote=[]
        list_magagine=[]
        list_confirm=[]
        for i in ransomNote:
            list_ransomNote.append(i)
        for i in magazine:
            list_magagine.append(i)            
        for i in list_ransomNote:
            if i in list_magagine:
                """list_ransomNote.pop(list_ransomNote.index(i))
                と直接for文の中のリストを変更するとバグる。
                https://qiita.com/tagtagtag/items/5ebf48af7c3fd4808525
                list_rasomNote[:]と全範囲スライスでコピーを作ってそれでfor文を
                回すか、下記のようにする"""
                list_confirm.append(i)
                list_magagine[list_magagine.index(i)]="$"
        return list_confirm == list_ransomNote

Solution().canConstruct("aaazx","aabqrsxza")
