# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from interpol.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from interpol.model.red_notice_detail import RedNoticeDetail
from interpol.model.red_notice_detail_arrest_warrants import RedNoticeDetailArrestWarrants
from interpol.model.red_notice_detail_embedded import RedNoticeDetailEmbedded
from interpol.model.red_notice_detail_images import RedNoticeDetailImages
from interpol.model.red_notice_detail_images_embedded import RedNoticeDetailImagesEmbedded
from interpol.model.red_notice_detail_images_embedded_images import RedNoticeDetailImagesEmbeddedImages
from interpol.model.red_notice_detail_images_embedded_links import RedNoticeDetailImagesEmbeddedLinks
from interpol.model.red_notice_detail_images_embedded_links_self import RedNoticeDetailImagesEmbeddedLinksSelf
from interpol.model.red_notice_detail_images_links import RedNoticeDetailImagesLinks
from interpol.model.red_notice_detail_images_links_notice import RedNoticeDetailImagesLinksNotice
from interpol.model.red_notice_detail_images_links_self import RedNoticeDetailImagesLinksSelf
from interpol.model.red_notice_detail_images_links_thumbnail import RedNoticeDetailImagesLinksThumbnail
from interpol.model.red_notice_detail_links import RedNoticeDetailLinks
from interpol.model.red_notices import RedNotices
from interpol.model.red_notices_embedded import RedNoticesEmbedded
from interpol.model.red_notices_links import RedNoticesLinks
from interpol.model.red_notices_links_self import RedNoticesLinksSelf
from interpol.model.red_notices_query import RedNoticesQuery
