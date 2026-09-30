import re
email_list = []
for text in text_list:
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    email_list.extend(emails)