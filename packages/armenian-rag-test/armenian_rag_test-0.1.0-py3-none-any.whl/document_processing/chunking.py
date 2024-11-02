import re
from config import CONFIG


class Chunking:
    def __init__(self):
        self.chunk_size = CONFIG['document']['chunk_size']


    def simple_splitter(self, text):
        chunks = []
        words = text.strip().split(" ")
        for i in range(0, len(words), self.chunk_size):
            chunks.append(" ".join(words[i:i+self.chunk_size]))
        return chunks
    
    
    def recursive_splitter(self, text):
        sentences = re.split(r"(?<=[։:])", text)
        chunks = []
        current_chunk = []
        current_length = 0
        for sentence in sentences:
            words = sentence.strip().split()
            if current_length + len(words) > self.chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_length = 0
            current_chunk.append(sentence)
            current_length += len(words)
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks
    