def domain_name(url):
  right_part = url.split('//')[-1]
  left_part = right_part.split('/')[0]
  left_part_no_www = left_part.replace('www.', '')
  domain_name_itself = left_part_no_www.split('.')[0]
  return domain_name_itself


if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
