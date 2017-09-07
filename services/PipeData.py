from MongoPipe import MongoPipe
from build_corpus import CorpusBuilder


class DataPipe:
    def __init__(self, pipe_to):
        self.pipe = MongoPipe(pipe_to)
        self.builder = CorpusBuilder()

    def execute_pipe(self, query, sort):
        total = self.builder.execute_query(query, sort, 0, 10000, 'total')
        selected_query = self.builder.execute_query(query, sort, 0, 10000)
        while not selected_query.extend_next() == len(total):
            selected_query = selected_query.extend_next()
            [self.pipe.pipe_data(item) for item in selected_query.extend_next()]


test_pipe = DataPipe('javascript')

print(test_pipe.execute_pipe('javascript', 'votes'))
