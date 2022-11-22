import random
import time
def shutudai(alphabet):
    all_chars = random.sample
    qa = random.choice(qa_lst)
    print("問題："+qa["q"])
    return abs

def kaitou(abs_chars):
    num = int(input("欠損文字はいくつあるでしょうか"))
    if num != num_of_abs_chars:
        print("不正解です。")
    else:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください。")
        ans = input(f"{i+1}一つ目の文字")
        if ans not in abs_chars:
            print

def alphabet():
    al = ["a","b","c","d","e","f","g"]
    for al in range(10):
        print("対象文字："+al)
        


if __name__=="__main__":
    qa_lst = [
        {"q":"欠損文字はいくつあるでしょうか？", "a":["alphabet"]}
    ]

    ans_lst = shutudai(qa_lst)
    if __name__=="__main__":
        alphabet = [chr(i+65) for i in range(num_of_alphabet)]
        for _ in range(num_of_trials):
            abs_chars = shutudai(alphabet)
            kaitou(abs_chars)
            if ret:
                break
            else:
                print("-"*20)
    
    ed =time.time()
    print(f"所要時間：{(ed-st):2f}秒")