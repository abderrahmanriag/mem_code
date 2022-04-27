from random import choices
from typing import List


Genome=List[int]
Population=List[Genome]
def generate_genome(length: int)->Genome:
                    return choices([0, 1], k=length)

def generate_population(size: int, genome_length: int)->Population:
                    return [generate_genome(genome_length) for _ in range(size)]