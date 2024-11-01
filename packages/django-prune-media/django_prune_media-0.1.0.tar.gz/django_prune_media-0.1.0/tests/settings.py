import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = Path(ROOT_DIR, "src")

DEBUG = bool(os.environ.get("DJANGO_DEBUG", 0))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "tests/purge_media.sqlite",
        "ATOMIC_REQUESTS": True,
    }
}

MEDIA_ROOT = str(ROOT_DIR / "media")

INSTALLED_APPS = ["prune_media", "tests.sample_app"]
