# choremonster-api
An unofficial Python API to access ChoreMonster

This screen-scraping API is brought to you by mechanize and BeautifulSoup.

Only supports `kids_login` and `get_chores` at this point.

Sample:
```python
import ChoreMonster
cm = ChoreMonster.ChoreMonster()
cm.kids_login("child_username", "child_password")
cm.get_chores()
```
