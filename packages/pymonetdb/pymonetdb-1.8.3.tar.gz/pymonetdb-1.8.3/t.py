#!/usr/bin/env python3

import pymonetdb

class MyDownloader(pymonetdb.Downloader):
    def __init__(self):
        self.downloaded = []

    def handle_download(self, download, filename,text_mode):
        self.downloaded.append(filename)
        print(self.downloaded)
        rd = download.binary_reader()
        while len(rd.read(1024)) > 0:
            pass


conn = pymonetdb.connect('demo', port=44001)
c1 = conn.cursor()
c2 = conn.cursor()

ddl = """
DROP TABLE IF EXISTS foo;
CREATE TABLE foo(i INT, j INT);
INSERT INTO foo 
    SELECT value as i, 10 * value as j
    FROM sys.generate_series(0, 10)
;
"""

c1.execute(ddl)

global_downloader = MyDownloader()

conn.set_downloader(global_downloader)


c1.execute("COPY SELECT i, j FROM foo INTO NATIVE ENDIAN BINARY 'i', 'j' ON CLIENT")
