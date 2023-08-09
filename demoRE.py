# demoRE.py 
import re 
#포함하고 있으면 검색 
result = re.search("[0-9]+th", "  35th")
print(result)
print(result.group())
#정확하게 일치 
# result = re.match("[0-9]+th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "빅테크에서 Apple의 위상".lower())
print(result.group())
print("---연도검색---")
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
print("---우편번호검색---")
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())

