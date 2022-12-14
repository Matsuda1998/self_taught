class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_chk =[]
        for i in range(len(s)):
            val = ""
            reverse_val =""
            for ch in s[i:]:
                val += ch
                reverse_val = val[::-1]
                if val == reverse_val:
                    list_chk.append(val)
        list_chk.sort(key=len,reverse=1)
        return list_chk[0]

a="""wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirl
jxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioa
gwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdc
tbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazj
pxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtw
dcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbe
imzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveu
rvrtvpvzbengdijkfcogpcrvwyf"""
Solution().longestPalindrome(a)
#できたけど長い奴がタイムオーバーになってsubmitできない。
b="cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"
Solution().longestPalindrome(b)
c="busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjnufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi"
Solution().longestPalindrome(c)
#提出用。･･･美しくない
class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_chk =[]
        for i in range(len(s)):
            val = ""
            reverse_val =""
            elm_chk = ""
            for ch in s[i:]:
                val += ch
                reverse_val = val[::-1]
                if val == reverse_val and len(val) > len(elm_chk):
                    elm_chk = val
            list_chk.append(elm_chk)
            if len(elm_chk) == len(s[i:]):
                break
        list_chk.sort(key=len,reverse=1)
        return list_chk[0]

d="reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"
Solution().longestPalindrome(d)
e="borcdubqiupahpwjizjjbkncelfazeqynfbrnzuvbhjnyvrlkdyfyjjxnprfocrmisugizsgvhszooktdwhehojbrdbtgkiwkhpfjfcstwcajiuediebdhukqnroxbgtvottummbypokdljjvnthcbesoyigscekrqswdpalnjnhcnqrarxuufzzmkwizptyvjhpfidgmskuaggtpxqisdlyloznkarxofzeeyvteynluofuhbllyiszszbwnsglqjkignusarxsjvctpgiwnhdufmfpanfwxjwlmhgllzsmdpncbwnsbdtsvrjybynifywkulqnzprcxockbhrhvnwxrkvwumyieazclcviumvormynbryaziijpdinwatwqppamfiqfiojgwkvfzyxadyfjrgmtttvlgkqghgbcfhkigfojjkhskzenlpasyozcsuccdxhulcubsgomvcrbqwakrraesfifecmoztayrdjicypakrrneulfbqqxtrdelggedvloebqaztmfyfkhuonrognejxpesmwgnmnnnamvkxqvzrgzdqtvuhccryeowywmbixktnkqnwzlzfvloyqcageugmjqihyjxhssmhkfzxpzxmgpjgsduogfolnkkqizitbvvgrkczmojxnabruwwzxxqcevdwvtiigwckpxnnxxxdhxpgomncttjutrsvyrqcfwxhexhaguddkiesmfrqfjfdaqbkeqinwicphktffuwcazlmerdhraufbpcznbuipmymipxbsdhuesmcwnkdvilqbnkaglloswcpqzdggnhjdkkumfuzihilrpcvemwllicoqiugobhrwdxtoefynqmccamhdtxujfudbglmiwqklriolqfkknbmindxtljulnxhipsieyohnczddabrxzjmompbtnnxvivmoyfzfrxlufowtqzojfclmatthjtbhotdoheusnpirwicbtyrcuojsdmfcx"
Solution().longestPalindrome(e)

#leetcodeの一番早い人のサンプル
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1 #i=1のとき l=0(1-1=0),r=2
            s1, s2 = s[l-1:r], s[l:r] #i=1のとき s1=[],s2=[0:2]
            
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start+size]
Solution().longestPalindrome("abb")

#動的計画法(Dynamic Programming)を解説したブログより　https://www.momoyama-usagi.com/entry/info-algo-dp
#フィボナッチ数列再帰法
def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
 
print(fib1(4))
#フィボナッチ数列メモ化再帰
memo = [0] *15
def fib2(n):
    print(memo)
    if n <= 1:
        return 1
    else:
        if memo[n] == 0:
            memo[n] = fib2(n-1) + fib2(n-2)
        return memo[n]
print(fib2(5))
memo[5]
#フィボナッチ数列動的計画法
def fib3(n):
    a = [1] *(n+1) # a[0],a[1]は1
    for i in range(2,n+1):
        a[i] = a[i-1]+a[i-2]
    return a[n]
print(fib3(5))

#動的計画法の例２（部分和問題）
#自分で考える(全点検索)
from typing import List
def sum_limit(num_list:List[int],limit:int)->int:
    num_sublist=[]
    for val in num_list:
        num_sublist.append([0,val])

    chk_list=num_sublist[0]
    for i in range(1,len(num_sublist)):
        temp_list=[]
        for j in range(len(chk_list)):
            for k in range(2):
                n=chk_list[j]+num_sublist[i][k]
                temp_list.append(n)
        chk_list=temp_list
    if limit in chk_list:
        return limit
    else:
        chk_list2=[]
        for val in chk_list:
            if val < limit :
                chk_list2.append(val)
        chk_list2.sort(reverse=1)
        return chk_list2[0]

sum_limit([6,8,4],10)

#動的計画法の例２（部分和問題）
#サイトの全点検索例（再帰法)*制限を超えたのは省くようにしている

def find_max_saiki(num_list,now,limit):
    list_len = len(num_list)
    if now >= list_len or limit <= 0:
        return 0 # これ以上追加できないとき or リストの最後尾まで探索終了
    else:
        tmp_not_choice = find_max_saiki(num_list,now + 1,limit)
        if num_list[now] > limit:
            return tmp_not_choice # now番目を追加できるようなコストがないとき
        else:
            tmp_choice = find_max_saiki(num_list,now + 1,limit - num_list[now]) + num_list[now]
            return max(tmp_choice,tmp_not_choice) # 追加 / 追加しない ときの2パターンを考える

find_max_saiki([6,8,4],0,10)

#動的計画法（部分和問題）
#サイトの例題を動的計画法で自分でコーディングしてみる！
def find_max_dp(num_list, limit):
    list_len=len(num_list)
    dp_list=[[0 for i in range(limit+1)] for j in range(list_len)]
    # 1番目の要素
    for i in range(limit+1):
        if i >= num_list[0]:
            dp_list[0][i]=num_list[0]
    # ２番目以降の要素
    for j in range(1,list_len):
        for i in range(num_list[j]):
            dp_list[j][i]=dp_list[j-1][i]
        for i in range(num_list[j],limit+1):
            if dp_list[j-1][i-num_list[j]] + num_list[j] >= dp_list[j-1][i]:
                dp_list[j][i] = dp_list[j-1][i-num_list[j]] + num_list[j]
            else:
                dp_list[j][i] = dp_list[j-1][i]

    return dp_list[list_len-1][limit]

find_max_dp([7,18,5,4,8],19) #出来たけどlimitより大きい値がnum_listに入っているとエラーが出る
                             #けど、今回問題ではそういつ設問はしないので、いいや。
    

