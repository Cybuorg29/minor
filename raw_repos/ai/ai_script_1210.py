def remove_comments(html_page):
  comment_start = "<!--"
  comment_end = "-->"
  output_page = ""
  while html_page:
    comment_start_index = html_page.find(comment_start)
    if comment_start_index == -1:
      output_page += html_page
      break
    output_page += html_page[:comment_start_index]
    html_page = html_page[comment_start_index:]
    comment_end_index = html_page.find(comment_end) + len(comment_end)
    html_page = html_page[comment_end_index:]
  
  return output_page