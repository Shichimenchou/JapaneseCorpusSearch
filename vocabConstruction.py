hiragana = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','は','ひ','ふ','へ','ほ','ま','み','む','め','も','な','に','ぬ','ね','の','ら','り','る','れ','ろ','や','よ','ゆ','ん','わ','を','が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ','だ','ぢ','づ','で','ど','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ','ゃ','ゅ','ょ','ゔ','ぁ','ぉ','ぇ','ぃ']
katakana = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ナ','ニ','ヌ','ネ','ノ','ラ','リ','ル','レ','ロ','ヤ','ヨ','ユ','ン','ワ','ヲ','ガ','ギ','ク','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ','ヅ','デ','ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ','ヤ','ュ','ョ','ヴ','ァ','ィ','ェ','ォ']
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ','ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ','Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ']
greek = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο']
numbers = ['0','1','2','3','4','5','6','7','8','9','０','１','２','３','４','５','６','７','８','９']
punctuation = ['/','\\','=','(',')','[',']','{','}','+','-','.',',','!','?','$','#','@','%','^','&','*','\'','"','|','<','>','／','＝','（','）','［','］','｛','｝','＋','−','．','，','！','？','＄','＃','＠','％','＾','＆','＊','’','”','｜','￥','＜','＞','。','「','」','｜','￥','…','〈','〉','〇','♪','；',':',';','、','~','`',' ']

kanji = {""}
nouns = {""}
verbs = {""}
loan = {""}
other = {""}

with open("corpus.utf") as f:
    corpus = f.readlines()

for line in corpus:
    for c in line:
        if c not in hiragana and c not in katakana and c not in english and c not in greek and c not in numbers and c not in punctuation:
            kanji.add(c)

for line in corpus:
    word = ""
    last = ""
    for c in line:
        if c in english or c in numbers or c in greek or c in punctuation:
            if word != "":
                if last in kanji:
                    nouns.add(word)
                elif last == "る" or last == "く" or last == "す" or last == "む" or last == "ぬ":
                    verbs.add(word)
                elif last in hiragana:
                    nouns.add(word)
                elif last in katakana:
                    loan.add(word)
                else:
                    other.add(word)
                word = ""
            continue
        if c in katakana:
            if last in katakana:
                word += c
                continue
            else:
                if word != "":
                    other.add(word)
                    word = ""
                    word += c
        if c not in katakana and last in katakana:
            loan.add(word)
            word = ""
            continue
        if c == 'を' or c == 'が' or c == 'は' or c == 'の':
            if last in kanji:
                nouns.add(word)
                word = ""
            elif last in hiragana:
                nouns.add(word)
                word = ""
                # Figure this out
                # !!!!!!!!!!!!!!!
        elif c == "る" or c == "く" or c == "す" or c == "む" or c == "ぬ":
            if last in kanji:
                word += c
                verbs.add(word)
                word = ""
            elif last in hiragana:
                verbs.add(word)
                word = ""
                # Figure this out
                # !!!!!!!!!!!!!!!
        elif c in kanji:
            if last == "と":
                word += c
                nouns.add(word)
                word = ""
            elif last in kanji:
                word += c
            elif last in hiragana:
                nouns.add(word)
                word = ""
                # Figure this one out
                # !!!!!!!!!!!!!!!!!!!
        #elif c in kanji:
        #    if last == "る" or last == "く" or last == "す" or last == "む" or last == "ぬ":
        #        nouns.add(word)
        #        word = ""
        #elif c in english or c in greek or c in punctuation or c in numbers:
        #    if last in kanji:
        #        nouns.add(word)
        #    elif last == "る" or last == "く" or last == "す" or last == "む" or last == "ぬ":
        #        verbs.add(word)
        #    other.add(word)
        #    word = ""
        else:
            word += c
        last = c
    other.add(word)

vocab = open("vocabulary.txt", "w")

v = open("verbs.txt", "w")
print("Below is the list of identified verbs:", file=v)
print("--------------------------------------", file=v)
for c in verbs:
    print(c, file=v)
    print(c, file=vocab)
n = open("nouns.txt", "w")
print("Below is the list of identified nouns:", file=n)
print("--------------------------------------", file=n)
for c in nouns:
    print(c, file=n)
    print(c, file=vocab)
l = open("loan.txt", "w")
print("Below is the list of identified loan words:", file=l)
print("-------------------------------------------", file=l)
for c in loan:
    print (c, file=l)
    print(c, file=vocab)
o = open("other.txt", "w")
print("Below is the list of unidentified Japanese word:", file=o)
print("------------------------------------------------", file=o)
for c in other:
    print(c, file=o)
