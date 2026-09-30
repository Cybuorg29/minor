emails = ["test@example.com", "example@example.org", "test@test.co.uk"]

from collections import defaultdict

by_domain = defaultdict(list)

for email in emails:
    domain = email.split("@")[-1]
    by_domain[domain].append(email)

print(dict(by_domain))