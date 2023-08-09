# 우리는 "re"라는 특별한 도구를 사용하여 텍스트에서 패턴을 찾는 데 도움을 받습니다.
import re

# 이 함수는 텍스트 안에서 이메일 주소를 찾는 데 도움을 줍니다.
def find_emails(text):
    # 이메일 패턴은 마치 이메일이 어떻게 생겼는지에 대한 레시피와 같습니다.
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # 레시피를 사용하여 텍스트 안에서 모든 이메일을 찾습니다.
    emails = re.findall(email_pattern, text, re.IGNORECASE)
    # 찾은 이메일 주소들의 목록을 반환합니다.
    return emails

# 이것들은 사람들이 쓸 수 있는 가짜 메시지입니다.
sample_texts = [
    "Please contact me at john.doe@example.com for more details.",
    "You can reach us at support@example.org if you have any questions.",
    "Email us at contact@company.net for inquiries.",
    "Feel free to email jane_smith123@gmail.com for assistance.",
    "For business inquiries, contact mike123@partners.co.uk.",
    "Reach out to us via email: info@website.com.",
    "Contact us at sales@productx.com to place your order.",
    "If you need help, email helpdesk@service.net.",
    "Email me at personal_email123@yahoo.com for a quick response.",
    "Please send your feedback to feedback@example.com."
]

# 이제 각 가짜 메시지를 하나씩 살펴보기 시작합니다.
for i, text in enumerate(sample_texts, start=1):
    # 어떤 샘플 메시지를 살펴보고 있는지 말합니다.
    print(f"샘플 {i}:\n{text}")
    # 함수를 사용하여 가짜 메시지 안에서 이메일 주소를 찾습니다.
    email_list = find_emails(text)
    # 만약 이메일을 찾았다면...
    if email_list:
        # 이메일을 찾았다고 말합니다!
        print("찾은 이메일 주소들:")
        # 그런 다음 찾은 각 이메일을 보여줍니다.
        for email in email_list:
            print(email)
    else:
        # 만약 이메일을 찾지 못했다면 그렇다고 말합니다.
        print("이메일 주소를 찾지 못했습니다.")
    # 예쁘게 보이게 공간을 남깁니다.
    print()
