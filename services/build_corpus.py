import stackexchange

class CorpusBuilder:
    def __init__(self):
        with open('key.txt') as key_file:
            for line in key_file:
                key = line.split(' ')[0]
                self.query_builder = stackexchange.Site(stackexchange.StackOverflow, impose_throttling=True)

    def execute_query(self, query, sortBy, minRange, maxRange, filterType=None):
        return self.query_builder.search(intitle=query, sort=sortBy, min=minRange, max=maxRange, has_more=True, page_size=100, page=1, filter=filterType)
