def LeapYearJudgement(year:int):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return "閏年"
    else:
        return "平年"

#--------------------------------------------------------------#

while True:
    print("閏年の判定を行います。（終了するには何も入力せずにEnterを入力してください。")
    print("年を入力してください。: ", end = "")
    try :
        year = input()
        
        if (year == ""):
            print("終了します。")
            break;        
        judge = LeapYearJudgement(int(year))
        print(judge + "です。")

    except:
        print("正しい数値が入力されませんでした。")