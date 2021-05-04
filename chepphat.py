import pyperclip #Module để lấy hàm copy
chep = input("Nhập câu cần chép: ")
so_lan = int(input("Nhập số lần: "))
ans = ""
for i in range(so_lan):
	ans+=(chep+"\n")

pyperclip.copy(ans)
print("Đã chép xong.")
input() #Dừng chương trình
