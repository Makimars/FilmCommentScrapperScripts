import requests
from bs4 import BeautifulSoup
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url_filmu = sys.argv[3]
##"https://www.csfd.cz/film/46838-laska-shora"

number_of_pages = int(sys.argv[2])

file_name = sys.argv[1]
count = 0

for i in range(number_of_pages):
    url = url_filmu + "/recenze/?page=" + str(i + 1) + "&sort=datetime_desc"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("ACCESS FAILED")
        exit()
    document = response.content

    soup = BeautifulSoup(document, 'html.parser')

    comments = soup.find_all("article", "article article-white")

    file = open(file_name, "a")
    for comment in comments:
        count += 1
        try:
            comment_text = str(comment.find('span', class_='comment').contents[0])
            comment_date = str(comment.find('span', class_='comment-date').time.contents[0])
            comment_author = comment.find('a', class_='user-title-name')['href']

            ## čsfd can have no rating on a comment
            rating = comment.find('span', class_='stars')
            if rating is not None:
                rating = str(rating['class'][1])
            else:
                rating = " "

            file.write(f"Review #{str(count)} \n")
            file.write(f"Page {str(i)} \n")
            file.write(f"Rating: {rating} \n")
            file.write(f"Review Text: {comment_text} \n")
            file.write(f"Review Date: {comment_date} \n")
            file.write("\n" + "-" * 50 + "\n")
        except:
            print(comment)
            exit(1)
    file.close()

    print(i)

print(count)
