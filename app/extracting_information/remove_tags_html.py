def parse_tag(soup, html_tag):
  
  label = [e.get_text() for e in soup.find_all(*html_tag)];
  
  label = '\n'.join(label);

  return label;