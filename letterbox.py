import requests
from bs4 import BeautifulSoup
import sys


def get_full_review_text(review_url):
    response = requests.get(review_url)
    return response.text


def get_reviews(url):
    reviews = []
    comment_count = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

    while url:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract reviews
        review_elements = soup.find_all('li', class_='film-detail')
        for review in review_elements:
            comment_count += 1
            user = review.find('strong', class_='name')
            rating = review.find('span', class_='rating')
            review_text_element = review.find('div', class_='body-text')
            review_date = review.find('span', class_='_nobr')

            # Check for "more" link
            more_link = review.find('div', class_='collapsed-text')
            if more_link:
                # Get the value of data-likeable-uid
                likeable_uid = review.find('p', class_='like-link-target')['data-likeable-uid']

                # Construct the URL for fetching full review text
                full_text_url = f'https://letterboxd.com/s/full-text/{likeable_uid}/'

                # Fetch the full review text
                full_review_text = get_full_review_text(full_text_url)

                # Update the review text with the full text
                review_text = full_review_text
            else:
                review_text = review_text_element.get_text(strip=True)

            reviews.append({
                'review_id': comment_count,
                'page': i,
                'review_on_page': None,
                'user': user.text if user else None,
                'rating': rating.text if rating else None,
                'review_text': review_text,
                'review_date': review_date.text
            })

        # Get next page URL
        next_page_link = soup.find('link', rel='next')
        url = next_page_link['href'] if next_page_link else None

    return reviews

# python letterbox.py file.txt 300 https://letterboxd.com/film/star-wars-episode-i-the-phantom-menace/reviews/by/activity/
resulting_file_name = sys.argv[1]
page_count = int(sys.argv[2])
film_url = sys.argv[3]
csf_format = True

for i in range(1, page_count):
    url = film_url
    if i > 1:
        url += "page/" + str(i)

    all_reviews = get_reviews(url)

    file = open(resulting_file_name, "a")

    for idx, review in enumerate(all_reviews, start=1):
        #print(review.keys())
        #print(review[list(review.keys())[0]])
        #print(review['review_id'])
        #print(review)
        file.write(f"Review #{str(review['review_id'])} \n")
        file.write(f"Page {review['page']}, Review on page {idx}: \n")
        file.write(f"User: {review['user']} \n")
        file.write(f"Rating: {review['rating']} \n")
        file.write(f"Review Text: {review['review_text']} \n")
        file.write(f"Review Date: {review['review_date']} \n")
        file.write("\n" + "-" * 50 + "\n")

    file.close()
    print(f"page {i} done")
