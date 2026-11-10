# 🎬 IMDb Scraper

IMDb Scraper is a **free and open-source** scraper that gets you **unlimited** detailed IMDb data for free.

## ✨ What Can I Get?

- 🔍 **Search 11M+ titles** — filter by type, genre, year; sort how you like
- 🎬 **Full title details** — cast, Metascore, box office, trailer & more
- 🖼️ **Title images** — direct image links, dimensions and captions
- 📺 **Episodes, reviews & people** — seasons, full review text, filmographies
- 📈 **All 6 IMDb charts** — Top 250s, Most Popular, Box Office, Celebrities

## 🎥 Example: A Full IMDb Movie

```json
{
  "id": "tt4154796",
  "title": "Avengers: Endgame",
  "link": "https://www.imdb.com/title/tt4154796/",
  "type": "movie",
  "year": 2019,
  "release_date": "2019-04-26",
  "runtime_minutes": 181,
  "certificate": "PG-13",
  "plot": "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
  "genres": ["Action", "Adventure", "Sci-Fi"],
  "rating": { "value": 8.4, "vote_count": 1480430, "top_rank": 74 },
  "metascore": { "score": 78, "review_count": 57 },
  "directors": [
    { "id": "nm0751577", "name": "Anthony Russo", "link": "https://www.imdb.com/name/nm0751577/" },
    { "id": "nm0751648", "name": "Joe Russo", "link": "https://www.imdb.com/name/nm0751648/" }
  ],
  "stars": [
    { "id": "nm0000375", "name": "Robert Downey Jr.", "link": "https://www.imdb.com/name/nm0000375/" },
    { "id": "nm0262635", "name": "Chris Evans", "link": "https://www.imdb.com/name/nm0262635/" }
  ],
  "top_cast": [
    {
      "id": "nm0000375",
      "name": "Robert Downey Jr.",
      "link": "https://www.imdb.com/name/nm0000375/",
      "characters": ["Tony Stark", "Iron Man"],
      "image": { "link": "https://m.media-amazon.com/images/M/MV5BNzg1MTUyNDYxOF5BMl5BanBnXkFtZTgwNTQ4MTE2MjE@._V1_.jpg" }
    }
  ],
  "trailer": {
    "id": "vi2163260441",
    "link": "https://www.imdb.com/video/vi2163260441/",
    "duration_seconds": 66
  },
  "box_office": {
    "budget": { "amount": 356000000, "currency": "USD" },
    "opening_weekend": { "amount": 357115007, "currency": "USD", "weekend_end_date": "2019-04-28", "theater_count": 4662 },
    "gross_worldwide": { "amount": 2799439100, "currency": "USD" }
  },
  "similar_titles": [
    { "id": "tt4154756", "title": "Avengers: Infinity War", "year": 2018, "rating": { "value": 8.4, "vote_count": 1403564 } }
  ],
  "countries_of_origin": ["United States"],
  "spoken_languages": ["English", "Japanese", "Xhosa"]
}
```

*Trimmed for readability.*

## 🚀 Unlimited Free IMDb Data — Get It in 60 Seconds

1️⃣ Clone and install:
```bash
git clone https://github.com/omkarcloud/imdb-scraper
cd imdb-scraper
python -m pip install -r requirements.txt
```

2️⃣ Start the API:
```bash
python run.py
```

3️⃣ Get your first data:
```bash
curl "http://localhost:8000/title/details?title_id=tt4154796"
```

```json
{
  "id": "tt4154796",
  "title": "Avengers: Endgame",
  "link": "https://www.imdb.com/title/tt4154796/",
  "type": "movie",
  "year": 2019,
  "release_date": "2019-04-26",
  "runtime_minutes": 181,
  "certificate": "PG-13",
  "genres": ["Action", "Adventure", "Sci-Fi"],
  "rating": { "value": 8.4, "vote_count": 1487872, "top_rank": 74 },
  "metascore": { "score": 78, "review_count": 57 },
  "directors": [
    { "id": "nm0751577", "name": "Anthony Russo", "link": "https://www.imdb.com/name/nm0751577/" },
    { "id": "nm0751648", "name": "Joe Russo", "link": "https://www.imdb.com/name/nm0751648/" }
  ],
  "box_office": {
    "budget": { "amount": 356000000, "currency": "USD" },
    "gross_worldwide": { "amount": 2799439100, "currency": "USD" }
  }
}
```

All 14 endpoints are now live at `http://localhost:8000`.

## 👀 Try It Without Installing

Want to check the data before setting anything up? The same API is hosted on RapidAPI.

1. [Subscribe to the free plan](https://rapidapi.com/OmkarCloud/api/imdb255/pricing) — 1,000 calls/month, no credit card.
2. [Open the playground](https://rapidapi.com/OmkarCloud/api/imdb255/playground/apiendpoint_ee818efa-c7bb-4e9e-b5ff-fe9d1e67ffa3) — Title Details is pre-filled with `tt4154796` (*Avengers: Endgame*). Click **Test Endpoint** to see the full response.
3. Change the parameters or pick another endpoint. All 13 have working example values.

Once you're happy with the data quality, run the open-source version above for **unlimited free** data.

## 📚 Endpoints

14 endpoints cover everything you need.

| Endpoint | Path | Returns |
|---|---|---|
| Title Details | `/title/details` | Everything about one title in a single call |
| Title Images | `/title/images` | Image links, dimensions and captions, 50 per page |
| Search Titles | `/search` | 50 titles per page; filter by type, genre, or year; sortable |
| Autocomplete | `/autocomplete` | Typeahead for titles and people |
| Title Cast | `/title/cast` | Full credits with character names, 50 per page |
| Title Reviews | `/title/reviews` | User reviews with full text, 25 per page |
| Title Episodes | `/title/episodes` | Season list, or one season's episodes with ratings |
| Person Details | `/person/details` | Bio, StarMeter rank, full filmography |
| Top 250 Movies / TV | `/charts/top-movies`, `/charts/top-tv` | All 250 in one call |
| Most Popular Movies / TV | `/charts/popular-movies`, `/charts/popular-tv` | MovieMeter / TVMeter top 100 |
| Weekend Box Office | `/charts/box-office` | US top 10 with weekend and worldwide gross |
| Popular Celebrities | `/charts/popular-celebrities` | StarMeter top 100 |

### Film image links

```bash
curl "http://localhost:8000/title/images?title_id=tt0111161"
```

Also available at `/imdb/title/images`. The required `title_id` accepts an
IMDb `tt` ID or a full IMDb title URL. Optional parameters are `country`
(two-letter code, default `US`) and `cursor` (the previous response's
`pagination.next_cursor`). Pass the cursor unchanged and URL-encode it when
building a query string.

The response contains `id`, `title`, `link`, `country`, `count`, `pagination`
and `results`. Each result contains `id`, `link` (the direct image URL),
`width`, `height`, `thumbnails` and `caption`. Images without a usable URL are skipped;
missing metadata is `null`. `pagination` contains `total`, `has_more` and
`next_cursor`; the cursor is `null` on the last page. A title with no images
returns an empty `results` list. Invalid parameters return HTTP 400 and
nonexistent titles return HTTP 404.

From Python:

```python
from imdb.title import get_title_images

page = get_title_images("tt0111161")
links = [image["link"] for image in page["results"]]
if page["pagination"]["has_more"]:
    next_page = get_title_images(
        "tt0111161", cursor=page["pagination"]["next_cursor"])
```


### Small images for compact lists

Image objects include a `thumbnails` map with direct IMDb CDN URLs for
96, 144 and 192 pixel widths. This applies to search, charts, details,
autocomplete, people and gallery results. No extra request to this API is
needed to get these URLs.

```json
{
  "link": "https://m.media-amazon.com/images/M/ASSET._V1_.jpg",
  "width": 1200,
  "height": 1800,
  "thumbnails": {
    "96": "https://m.media-amazon.com/images/M/ASSET._V1_SX96_.jpg",
    "144": "https://m.media-amazon.com/images/M/ASSET._V1_SX144_.jpg",
    "192": "https://m.media-amazon.com/images/M/ASSET._V1_SX192_.jpg"
  }
}
```

`ASSET` is illustrative. `link`, `width` and `height` describe the original
image. Thumbnail URLs request width-only resizing, preserving the source
aspect ratio; height is not fixed and existing CDN crop instructions are
replaced. Only recognized HTTPS IMDb CDN JPEG URLs receive variants;
other URL formats have `thumbnails: {}`. Missing images remain `null`.

For native mobile lists, multiply the displayed width in points by the
device scale, then choose the smallest sufficient variant, capped at 192px.
A 48-point poster uses `thumbnails["96"]` at 2× or `thumbnails["144"]` at 3×.
For displays requiring more than 192px, use the original `link`.
Cache downloaded images by variant URL and downsample during decoding to
limit memory use. Fit or crop the image in the UI as needed.

IMDb's CDN transformation convention is not a guaranteed public API. Show
a placeholder if a thumbnail fails to load or no suitable URL is available.
Our backend generates URLs only; image downloads go directly to IMDb's CDN.

## 🔍 Exploring Parameters

The same API is published on RapidAPI, and its playground is the easiest place to try parameters and see raw responses. Once a request looks right, run it locally for **unlimited free** data.

1. [Subscribe to the free plan](https://rapidapi.com/OmkarCloud/api/imdb255/pricing) — 1,000 calls/month, no credit card.
2. [Try the endpoints in the playground](https://rapidapi.com/OmkarCloud/api/imdb255/playground/apiendpoint_ee818efa-c7bb-4e9e-b5ff-fe9d1e67ffa3) — every param is pre-filled, so you see real data in one click.
3. Copy the generated code and replace `https://imdb255.p.rapidapi.com` with `http://localhost:8000`. It will now run against your local API.

```python
import requests

# generated by the playground, host swapped for the local API
response = requests.get(
    "http://localhost:8000/title/details",
    params={"title_id": "tt4154796"},
)
print(response.json())
```

## 💬 Have Questions? We Have Answers.

You're a developer — we know how hard completing a project can be. So we offer full support: just message us and we'll reply ✅ with a solution within 1 working day.

[![Message Us on WhatsApp about IMDb Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20need%20help%20using%20the%20IMDb%20Scraper%20API.)

[![Ask Us by Email about IMDb Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=Help%20with%20IMDb%20Scraper%20API&body=I%20need%20help%20using%20the%20IMDb%20Scraper%20API.)

## ⚡ Popular Scrapers by Omkar Cloud

- [**Google Maps Scraper (3,100+ GitHub Stars)**](https://github.com/omkarcloud/google-maps-scraper) — type "dentists in New York", get every business as a ready-to-call lead list: phones, emails, websites & reviews. Up to 100K free leads/month.
- [**G2 Scraper**](https://www.omkar.cloud/tools/g2-scraper) — G2 product details, ratings & AI-found contacts
- [**Website Email Contact Scraper**](https://www.omkar.cloud/tools/website-email-contact-scraper) — emails, phones & socials from any website
- [**AliExpress Scraper**](https://www.omkar.cloud/tools/aliexpress-scraper) — live product details, SKU variants, stock & shipping
- [**Booking Scraper**](https://www.omkar.cloud/tools/booking-scraper) — Booking.com hotels: prices, ratings, rooms & amenities
- [**Etsy Scraper**](https://www.omkar.cloud/tools/etsy-scraper) — Etsy products: prices, discounts, shops & variations

## ⭐ Love It? [Star It ⭐!](https://github.com/omkarcloud/imdb-scraper)

Star the repo ⭐ and become my star hero!

It's just 1 click, but it means the world to me.

[![Star us on GitHub](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/star-us.png)](https://github.com/omkarcloud/imdb-scraper)
