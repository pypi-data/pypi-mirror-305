# URLs

Types:

```python
from sst_url_shortener.types import (
    ShortURL,
    ShortURLCountResult,
    ShortURLSearchResult,
    URLCreateResponse,
    URLDeleteByOriginalURLResponse,
    URLDeleteByShortIDResponse,
    URLFromOriginalURLResponse,
    URLFromShortIDResponse,
    URLQuickCountResponse,
    URLSearchResponse,
    URLSlowCountResponse,
)
```

Methods:

- <code title="post /urls/create">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">create</a>(\*\*<a href="src/sst_url_shortener/types/url_create_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_create_response.py">URLCreateResponse</a></code>
- <code title="delete /urls/delete-by-original-url">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">delete_by_original_url</a>(\*\*<a href="src/sst_url_shortener/types/url_delete_by_original_url_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_delete_by_original_url_response.py">object</a></code>
- <code title="delete /urls/delete-by-short-id">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">delete_by_short_id</a>(\*\*<a href="src/sst_url_shortener/types/url_delete_by_short_id_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_delete_by_short_id_response.py">object</a></code>
- <code title="get /urls/from-original-url">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">from_original_url</a>(\*\*<a href="src/sst_url_shortener/types/url_from_original_url_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_from_original_url_response.py">URLFromOriginalURLResponse</a></code>
- <code title="get /urls/from-short-id">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">from_short_id</a>(\*\*<a href="src/sst_url_shortener/types/url_from_short_id_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_from_short_id_response.py">URLFromShortIDResponse</a></code>
- <code title="get /urls/quick-count">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">quick_count</a>() -> <a href="./src/sst_url_shortener/types/url_quick_count_response.py">URLQuickCountResponse</a></code>
- <code title="get /urls/search">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">search</a>(\*\*<a href="src/sst_url_shortener/types/url_search_params.py">params</a>) -> <a href="./src/sst_url_shortener/types/url_search_response.py">URLSearchResponse</a></code>
- <code title="get /urls/slow-count">client.urls.<a href="./src/sst_url_shortener/resources/urls.py">slow_count</a>() -> <a href="./src/sst_url_shortener/types/url_slow_count_response.py">URLSlowCountResponse</a></code>
