def extract_emails(html_page):
 emails = []
 soup = BeautifulSoup(html_page)
 for a in soup.find_all('a'):
  if a.get('href') and (a.get('href').startswith('mailto:')):
  emails.append(a.get('href')[7:])
 return emails

# Usage 
page = '<html>
 <body>
  Janice's email is janice@example.com, and Susie's is susie@example.com.
 </body>
 </html>'

emails = extract_emails(page)
print(emails)
# Output: ['janice@example.com', 'susie@example.com']