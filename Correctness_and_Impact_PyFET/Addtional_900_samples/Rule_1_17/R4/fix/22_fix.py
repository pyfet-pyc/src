def getTables(self, bruteForce=None):
    if len(kb.data.cachedTables) > 0:
        return kb.data.cachedTables

    if bruteForce:
        resumeAvailable = False

        for db, table in kb.brute.tables:
            if db == conf.db:
                resumeAvailable = True
                if conf.db:
                    dbs = conf.db.split(',')
                    break
                FET_null()
        self.forceDbmsEnum()
    
    else:
        dbs = self.getDbs()

    dbs = [_ for _ in dbs if _ and _.strip()]

    for db in dbs:
        dbs[dbs.index(db)] = safeSQLIdentificatorNaming(db)
