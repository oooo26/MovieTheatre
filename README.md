# Movie Theatre

This is project 2 for DSA5101: use Django to build a movie theatre site.

## Quick Start

1. Install [supported database](https://docs.djangoproject.com/en/4.1/topics/install/#database-installation) and re-configure `settings.py`;

2. (Optional) Install [selenium](https://pypi.org/project/selenium/), [ChromeDriver](https://chromedriver.chromium.org/), [pyquery](https://pypi.org/project/pyquery/) to support "Add movie from GV link";
3. Migrate database and django project:

   ```bash

   $ python manage.py makemigrations about
   $ python manage.py migrate

   ```
4. Create [super user](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#creating-an-admin-user) for admin site;
5. Load `saved_data.json` for some simple examples:

   ```bash

   $ python manage.py loaddata saved_data.json

   ```
6. Run server:

   ```bash

   $ python manage.py runserver

   ```

## Site Structure

- `/`: Redirect to `/about-us/`;
- `/admin/`: Admin site. (Log in with super user.)
- `/about-us/`: About us page;
- `/about-us/movie/`: Movie theatre page;
- `/about-us/movie/subsribe/`: Subscribe new movie;

## TODO list

- [x] Out of bound if movie title is too long;
- [x] Spacing in rows;
- [x] Duplicate items if add twice;
- [x] Feedback message;
- [x] Better navigation;
- [ ] Better description/theme/layout;
- [ ] Check wrong input;
- [ ] Pool coding :smiling_face_with_tear:;
- [ ] Search bar;
- [ ] Favorites;
- [ ] ...

## Contributors

- Shen Shuyuan
- Wang Yuhua
- Chen Yanrong
- Huang Junhao
