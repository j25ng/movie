# movie

### install
```bash
# main
$ pip install git+https://github.com/j25ng/movie.git

# branch
$ pip install git+https://github.com/j25ng/movie.git@<BRANCH_NAME>
```

### start dev
```bash
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install
$ pytest

# option
$ pdm venv create
```

### setting env
```bash
$ cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"
```
