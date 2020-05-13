import time
from konlpy.tag import Kkma, Okt, Komoran

km = Kkma()
similarty = []
arr=[]
texts = open('input3.txt')


def RunningSpeed():   
    pos_taggers = [('kkma', Kkma()), ('Okt', Okt()), ('Komoran', Komoran())]
    results = []
    for name, tagger in pos_taggers:
        tokens = []
        process_time = time.time()
        texts = open('input3.txt')
        for text in texts:
            testLine = texts.readline()
            n = km.morphs(testLine)
        process_time = time.time() - process_time
        print('tagger name = %10s, %.3f secs' % (name, process_time))
        results.append(tokens)

def Jaccard_similarty(text1,text2):
    res = set(text1).union(set(text2))
    intersection = set(text1).intersection(set(text2))
    similarty.append(len(intersection)/len(res))
    #print(similarty)
   

def accuracy(name):
    reslut = []
    if name == 'kma':
        mode = Kkma()
    elif name == 'okt':
        mode = Okt()
    elif name == 'komoran':
        mode = Komoran()
    else :
        return 0
    
    mylin = input ("문장을 입력해 주세요: " )
    
    print("형태소분석기",name,"정확도 분석을 시작합니다. ")
    print('\n')
    acc = mode.morphs(mylin) # 입력문장 형태소 분석
    for sentence in texts:
        arr.append(sentence)
        sp_text = mode.morphs(sentence) # 한줄씩 문장별로 잘라서 형태소 분석
        Jaccard_similarty(acc,sp_text) # 자칼드 유사도로 유사도 계산
    
    n = 5
    Sortsimilarty = sorted(range(len(similarty)),key=lambda i: similarty[i], reverse=True)[:n] # 결과를 sort 해줍니다.
    
    k = 0
    for i in Sortsimilarty:
        k = k+1
        print( k ,"번째로 유사도가 높은 문장입니다. : ",arr[i],"유사도는 다음과 같습니다. : ", similarty[i] )
        
    print('\n')
    Sortsimilarty = []
    similarty = []

if __name__ == '__main__':
    #RunningSpeed()
    accuracy('kma')
    accuracy('okt')
    accuracy('komoran')
    
