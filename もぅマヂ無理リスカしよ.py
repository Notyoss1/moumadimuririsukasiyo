import time

waitsec = float(input("回答後何秒待ちますか?"))
answer = str(input("もぅマヂ無理?(y/n)"))
if answer == "y":
    print("もぅマヂ無理リスカしよ")

print(waitsec,"秒後に終了します...")
time.sleep(waitsec)