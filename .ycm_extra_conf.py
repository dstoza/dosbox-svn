def FlagsForFile(filename, **kwargs):
    root = '/home/stoza/dosbox-svn'
    return {
        'flags': [
            '-I', root,
            '-I', root + '/include',
            '-I/usr/include/SDL',
        ]
    }
