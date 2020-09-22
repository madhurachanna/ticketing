import shortuuid


def genereate_uuid(length=15):
    return shortuuid.ShortUUID().random(length=length)
